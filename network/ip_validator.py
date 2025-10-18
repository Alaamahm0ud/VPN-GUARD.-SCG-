# =========================================================
#  VPN GUARD (SCG) - IP Validator
#  Checks and validates IP addresses and domains for trustworthiness.
# =========================================================

import ipaddress

class IPValidator:
    def __init__(self):
        self.blocked_ranges = ["192.168.0.0/24", "10.0.0.0/8"]

    def is_valid(self, ip):
        try:
            ipaddress.ip_address(ip)
            for blocked in self.blocked_ranges:
                if ipaddress.ip_address(ip) in ipaddress.ip_network(blocked):
                    print(f"[IPValidator] IP {ip} blocked (in private range).")
                    return False
            print(f"[IPValidator] IP {ip} valid.")
            return True
        except ValueError:
            print(f"[IPValidator] Invalid IP format: {ip}")
            return False
