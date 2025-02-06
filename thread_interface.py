from threading import Thread


class TaskController:

    def __init__(self, target):
        self.periodic_thread = Thread(target=target, daemon=True) 

    def start_task(self):
        self.periodic_thread.start()

    def suspend_task(self):
        pass

    def resume_task(self):
        pass