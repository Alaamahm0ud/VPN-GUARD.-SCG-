# =========================================================
#  VPN GUARD (SCG) - Main Entry Point
#  Author: Alaa Mahmoud Mohamed
#  Description: Launches core modules and initializes system.
# =========================================================

from core.engine import SCGEngine

if __name__ == "__main__":
    print("🛡️  Starting VPN GUARD (SCG) ...")
    scg = SCGEngine()
    scg.start()
