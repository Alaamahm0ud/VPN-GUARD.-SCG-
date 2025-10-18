# ======================================================
#  VPN GUARD (SCG)
#  Module: CacheManager
#  Author: Alaa Mahmoud Mohamed
#  Description:
#     High-performance asynchronous cache system
#     supporting both local in-memory and Redis storage.
# ======================================================

import asyncio
import time
import hashlib
from typing import Any, Optional

try:
    import redis.asyncio as redis
except ImportError:
    redis = None


class CacheManager:
    """
    Unified async cache handler for VPN GUARD (SCG).
    Supports both local cache and Redis backend.
    """

    def __init__(self, use_redis: bool = False, redis_url: str = "redis://localhost:6379"):
        self.use_redis = use_redis and redis is not None
        self.local_cache = {}
        self.redis_url = redis_url
        self.ttl_cleanup_interval = 60
        self._cleanup_task = None
        if self.use_redis:
            self.redis_client = redis.from_url(redis_url, decode_responses=True)
        else:
            self.redis_client = None

    async def start_cleanup_task(self):
        """Run periodic cleanup for expired local cache entries."""
        async def cleanup():
            while True:
                now = time.time()
                expired_keys = [k for k, v in self.local_cache.items() if v["expires_at"] < now]
                for key in expired_keys:
                    self.local_cache.pop(key, None)
                await asyncio.sleep(self.ttl_cleanup_interval)

        if not self._cleanup_task:
            self._cleanup_task = asyncio.create_task(cleanup())

    def _generate_key(self, data: str) -> str:
        """Generate SHA256 key for consistent caching."""
        return hashlib.sha256(data.encode()).hexdigest()

    async def set(self, key: str, value: Any, ttl: int = 300):
        """Store a key-value pair with optional expiration (TTL)."""
        cache_key = self._generate_key(key)
        if self.use_redis and self.redis_client:
            await self.redis_client.set(cache_key, str(value), ex=ttl)
        else:
            self.local_cache[cache_key] = {"value": value, "expires_at": time.time() + ttl}

    async def get(self, key: str) -> Optional[Any]:
        """Retrieve cached value if available and valid."""
        cache_key = self._generate_key(key)
        if self.use_redis and self.redis_client:
            result = await self.redis_client.get(cache_key)
            return result
        else:
            item = self.local_cache.get(cache_key)
            if item and item["expires_at"] > time.time():
                return item["value"]
            self.local_cache.pop(cache_key, None)
            return None

    async def clear(self):
        """Clear entire cache (local or Redis)."""
        if self.use_redis and self.redis_client:
            await self.redis_client.flushdb()
        else:
            self.local_cache.clear()

    async def stop(self):
        """Gracefully stop cleanup task."""
        if self._cleanup_task:
            self._cleanup_task.cancel()
        if self.use_redis and self.redis_client:
            await self.redis_client.close()


# ======================================================
# Example Usage (Development)
# ======================================================
if __name__ == "__main__":
    async def demo():
        cache = CacheManager(use_redis=False)
        await cache.start_cleanup_task()
        await cache.set("session_1", {"user": "alpha", "status": "active"}, ttl=5)
        result = await cache.get("session_1")
        print("Cached Result:", result)
        await asyncio.sleep(6)
        expired = await cache.get("session_1")
        print("After Expiration:", expired)

    asyncio.run(demo())
