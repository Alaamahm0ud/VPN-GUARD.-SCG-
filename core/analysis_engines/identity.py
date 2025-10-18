# =========================================================
#  VPN GUARD (SCG) - Identity Management Engine
# =========================================================

class IdentityManagementEngine:
    def __init__(self):
        self.valid_sessions = []

    def verify_session(self, session_id):
        if session_id in self.valid_sessions:
            print(f"[IdentityEngine] Session {session_id} valid.")
            return True
        print(f"[IdentityEngine] Session {session_id} invalid.")
        return False

    def add_session(self, session_id):
        self.valid_sessions.append(session_id)
        print(f"[IdentityEngine] Session {session_id} added.")
