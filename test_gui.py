import tkinter as tk
import threading
import time
import queue

def worker(q):
    # Symulacja długotrwałej operacji
    time.sleep(3)
    q.put("Operacja zakończona!")

def update_gui():
    try:
        msg = q.get_nowait()
        label.config(text=msg)
    except queue.Empty:
        root.after(100, update_gui)

root = tk.Tk()
root.title("Wielowątkowość w Tkinter")

q = queue.Queue()

label = tk.Label(root, text="Czekam na wynik...")
label.pack()

# Uruchamiamy wątek roboczy
thread = threading.Thread(target=worker, args=(q,))
thread.start()

# Uruchamiamy cykliczną funkcję, która będzie sprawdzać wynik
root.after(100, update_gui)

root.mainloop()