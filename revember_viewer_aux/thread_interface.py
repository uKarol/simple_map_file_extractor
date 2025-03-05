import multiprocessing
import threading


class TaskController:

    def __init__(self, task_run):

        self.task_run = task_run
        self.control_event = threading.Event()
        self.control_event.clear()
        self.stop_event = threading.Event()
        self.stop_event.clear()
        self.periodic_task = threading.Thread(target=self.generic_task, daemon=False)
        self.terminate_task = False

    def start_task(self):
        self.periodic_task.start()

    def suspend_task(self):
        self.control_event.clear()

    def resume_task(self):
        self.control_event.set()

    def finish_task(self):
        self.stop_event.set()
        self.control_event.set()
        print("finishing")
        #self.periodic_task.join()

    def generic_task(self):
        while self.control_event.wait():
            if self.stop_event.is_set():
                print("finishing")
                return
            self.task_run()