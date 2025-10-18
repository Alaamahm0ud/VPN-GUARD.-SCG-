# =========================================================
#  VPN GUARD (SCG) - Packet Monitor
#  Monitors and analyzes real-time network packets for anomalies.
# =========================================================

import random

class PacketMonitor:
    def __init__(self, analyzer):
        self.analyzer = analyzer

    def capture(self):
        simulated_packets = [
            "GET /index.html",
            "POST /login malicious attempt",
            "DATA normal packet",
            "PING clean request"
        ]
        print("[Monitor] Capturing packets...")
        for packet in simulated_packets:
            time_delay = random.uniform(0.1, 0.3)
            self.analyzer.scan_traffic(packet)
        print("[Monitor] Capture cycle complete.")
