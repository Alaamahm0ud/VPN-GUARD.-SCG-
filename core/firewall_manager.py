# =========================================================
#  VPN GUARD (SCG) - Firewall Manager
#  Handles traffic filtering, IP blocking, and system defense.
# =========================================================

class FirewallManager:
    def __init__(self):
        self.rules = []

    def load_rules(self):
        print("[Firewall] Loading protection rules...")
        # Placeholder for real firewall logic
        self.rules = ["ALLOW localhost", "BLOCK suspicious_ips"]

    def apply_rule(self, rule):
        print(f"[Firewall] Applying rule: {rule}")
        self.rules.append(rule)
