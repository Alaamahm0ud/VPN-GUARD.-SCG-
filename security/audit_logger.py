# =========================================================
#  VPN GUARD (SCG) - Audit Logger
#  Logs system events, security actions, and anomalies for review.
# =========================================================

import datetime

class AuditLogger:
    def __init__(self, logfile="logs/security_audit.log"):
        self.logfile = logfile

    def log_event(self, event):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {event}\n"
        with open(self.logfile, "a") as log:
            log.write(log_entry)
        print(f"[Audit] Logged: {event}")
