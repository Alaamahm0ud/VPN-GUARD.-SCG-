# =========================================================
#  VPN GUARD (SCG) - Firewall Manager
#  Manages custom firewall rules for inbound/outbound traffic.
# =========================================================

class FirewallManager:
    def __init__(self):
        self.rules = []

    def apply_rule(self, rule):
        self.rules.append(rule)
        print(f"[Firewall] Rule applied: {rule}")

    def remove_rule(self, rule):
        if rule in self.rules:
            self.rules.remove(rule)
            print(f"[Firewall] Rule removed: {rule}")

    def show_rules(self):
        print(f"[Firewall] Active rules: {len(self.rules)}")
        for r in self.rules:
            print(f"  - {r}")
        return self.rules
