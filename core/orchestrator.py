# =========================================================
#  VPN GUARD (SCG) - Orchestrator
#  Coordinates tasks, engines, and adaptive routing.
# =========================================================

from collections import deque

class AegisOrchestrator:
    def __init__(self):
        self.task_queue = deque()
        self.health_flag = True

    def add_task(self, task):
        self.task_queue.append(task)
        print(f"[Orchestrator] Task added. Queue size: {len(self.task_queue)}")

    def process_tasks(self):
        while self.task_queue:
            task = self.task_queue.popleft()
            try:
                task()
            except Exception as e:
                print(f"[Orchestrator] Error executing task: {e}")
                self.health_flag = False
