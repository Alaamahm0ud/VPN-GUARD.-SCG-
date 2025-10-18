# =========================================================
#  VPN GUARD (SCG) - Deception Engine
# =========================================================

class DeceptionEngine:
    def generate_decoy(self, request):
        decoy = f"decoy_for_{request}"
        print(f"[DeceptionEngine] Generated decoy: {decoy}")
        return decoy
