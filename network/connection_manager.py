# =========================================================
#  VPN GUARD (SCG) - Connection Manager
#  Handles secure VPN connections and session lifecycle.
# =========================================================

import time
import random

class ConnectionManager:
    def __init__(self):
        self.active_connections = {}

    def connect(self, user_id):
        session_id = f"SCG-{random.randint(1000,9999)}"
        self.active_connections[user_id] = session_id
        print(f"[Connection] User {user_id} connected with session {session_id}.")
        return session_id

    def disconnect(self, user_id):
        if user_id in self.active_connections:
            del self.active_connections[user_id]
            print(f"[Connection] User {user_id} disconnected.")
        else:
            print(f"[Connection] No active session found for {user_id}.")

    def list_active(self):
        print(f"[Connection] Active sessions: {len(self.active_connections)}")
        return self.active_connections
