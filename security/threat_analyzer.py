# =========================================================
#  VPN GUARD (SCG) - Threat Analyzer
#  Analyzes incoming/outgoing traffic and detects anomalies.
# =========================================================

class ThreatAnalyzer:
    def __init__(self):
        self.alerts = []

    def scan_traffic(self, packet):
        if "malicious" in packet.lower():
            self.alerts.append(packet)
            print(f"[Threat] Suspicious activity detected: {packet}")
        else:
            print(f"[Traffic] Clean packet: {packet}")

    def report(self):
        print(f"[Threat Report] Total alerts: {len(self.alerts)}")
        return self.alerts
