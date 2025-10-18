# =========================================================
#  VPN GUARD (SCG) - Aegis Guardian Bot
#  Continuously monitors system health and alerts anomalies.
# =========================================================

import threading
import time

class AegisGuardian:
    def __init__(self, orchestrator):
        self.orchestrator = orchestrator
        self.running = False

    def start(self):
        self.running = True
        thread = threading.Thread(target=self.monitor_loop, daemon=True)
        thread.start()
        print("[AegisGuardian] Monitoring started.")

    def monitor_loop(self):
        while self.running:
            health = self.orchestrator.health_flag
            queue_size = len(self.orchestrator.task_queue)
            if health is False or queue_size > 100:
                print(f"[AegisGuardian Alert] Health: {health}, Queue Size: {queue_size}")
            time.sleep(1)

    def stop(self):
        self.running = False
        print("[AegisGuardian] Monitoring stopped.")
