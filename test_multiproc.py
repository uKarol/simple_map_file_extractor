import multiprocessing
import time

def control_process(process, pause_event):
    """
    Receive a process object as an argument and provides the ability
    to pause and resume the process.
    """
    while True:
        command = input("Enter 'p' to pause, 'r' to resume, or 'q' to quit: ")
        print(command)
        if command == "p":
            pause_event.clear()
        elif command == "r":
            pause_event.set()
        elif command == "q":
            process.terminate()
            break

def my_function(pause_event, event_started):
    event_started.set()  # signal parent that it has started execution
    while pause_event.wait():  # returns True if pause_event is set
        print("Hello, world!")
        time.sleep(1)
if __name__ == "__main__":
    pause_event = multiprocessing.Event()
    started_event = multiprocessing.Event()  # to know when the child started execution
    # consider making this next process daemon for guaranteed cleanup
    p = multiprocessing.Process(target=my_function, args=(pause_event, started_event))
    p.start()

    started_event.wait(timeout=5)  # to fix window's buggy terminal
    control_process(p, pause_event)