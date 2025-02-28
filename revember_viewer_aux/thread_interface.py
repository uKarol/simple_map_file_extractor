import multiprocessing
import threading


class TaskController:

    def __init__(self, task_run):

        self.task_run = task_run
        self.control_event = threading.Event()
        self.control_event.clear()
        self.periodic_task = threading.Thread(target=self.generic_task, daemon=True)

    def start_task(self):
        self.periodic_task.start()

    def suspend_task(self):
        self.control_event.clear()

    def resume_task(self):
        self.control_event.set()

    def generic_task(self):
        while self.control_event.wait():
            self.task_run()