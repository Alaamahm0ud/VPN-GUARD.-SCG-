# ======================================================
#  VPN GUARD (SCG)
#  Module: SecurityUtils
#  Author: Alaa Mahmoud Mohamed
#  Description:
#     Provides lightweight security analysis utilities for
#     data validation, integrity checking, and anomaly detection.
# ======================================================

import re
import hashlib
import base64
import time
from typing import Any, Dict


class SecurityUtils:
    """
    Core utility class providing basic security functions
    used throughout the VPN GUARD (SCG) framework.
    """

    @staticmethod
    def sanitize_input(data: str) -> str:
        """Remove any unwanted control characters or escape sequences."""
        if not isinstance(data, str):
            return ""
        sanitized = re.sub(r"[^\w\s\-_.:/@]", "", data)
        return sanitized.strip()

    @staticmethod
    def hash_data(data: str) -> str:
        """Generate a secure SHA256 hash for given input."""
        if not isinstance(data, str):
            data = str(data)
        return hashlib.sha256(data.encode("utf-8")).hexdigest()

    @staticmethod
    def encode_base64(data: str) -> str:
        """Safely encode text to Base64."""
        return base64.b64encode(data.encode()).decode()

    @staticmethod
    def decode_base64(data: str) -> str:
        """Safely decode Base64-encoded text."""
        try:
            return base64.b64decode(data.encode()).decode()
        except Exception:
            return ""

    @staticmethod
    def detect_anomaly(packet_meta: Dict[str, Any]) -> bool:
        """
        Lightweight heuristic anomaly detection.
        Used for early warning within routing or identity layers.
        """
        if not packet_meta:
            return False

        # Example checks (to be expanded in later releases)
        unusual_size = packet_meta.get("size", 0) > 10_000_000
        repeated_source = packet_meta.get("retries", 0) > 5
        suspicious_pattern = bool(re.search(r"(malware|phish|botnet)", packet_meta.get("payload", ""), re.I))

        return any([unusual_size, repeated_source, suspicious_pattern])

    @staticmethod
    def get_timestamp() -> str:
        """Return current UTC timestamp (formatted)."""
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())


# ======================================================
# Example Usage
# ======================================================
if __name__ == "__main__":
    text = "example_payload@domain.com"
    print("Sanitized:", SecurityUtils.sanitize_input(text))
    print("Hash:", SecurityUtils.hash_data(text))
    encoded = SecurityUtils.encode_base64(text)
    print("Encoded:", encoded)
    print("Decoded:", SecurityUtils.decode_base64(encoded))

    test_packet = {"size": 12000, "retries": 2, "payload": "test malware link"}
    print("Anomaly detected:", SecurityU
