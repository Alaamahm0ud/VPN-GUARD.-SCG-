# =========================================================
#  VPN GUARD (SCG) - Adaptive Router
#  Generates random routes and applies encryption for traffic.
# =========================================================

import random

class AdaptiveRouter:
    def __init__(self):
        self.routes = ["NodeA", "NodeB", "NodeC", "NodeD"]

    def get_route(self):
        route = random.choice(self.routes)
        print(f"[AdaptiveRouter] Selected route: {route}")
        return route

    def route_packet(self, packet):
        route = self.get_route()
        print(f"[AdaptiveRouter] Routing packet '{packet}' via {route}")
        # Placeholder for real routing logic
