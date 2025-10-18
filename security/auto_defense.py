# =========================================================
#  VPN GUARD (SCG) - Auto Defense System
#  Automatically responds to detected threats and enforces rules.
# =========================================================

class AutoDefense:
    def __init__(self, firewall, analyzer):
        self.firewall = firewall
        self.analyzer = analyzer

    def respond(self):
        for alert in self.analyzer.alerts:
            rule = f"BLOCK {alert}"
            print(f"[AutoDefense] Responding to threat: {alert}")
            self.firewall.apply_rule(rule)
        print("[AutoDefense] Response cycle completed.")
