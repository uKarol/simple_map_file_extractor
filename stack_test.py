from tkinter import *

root = Tk()
frame = Frame(root)
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
frame.grid(row=0, column=0, sticky="news")
grid = Frame(frame)
grid.grid(sticky="news", column=0, row=7, columnspan=2)
frame.rowconfigure(7, weight=1)
frame.columnconfigure(0, weight=1)

#example values
for x in range(10):
    for y in range(5):
        btn = Button(frame)
        btn.grid(column=x, row=y, sticky="news")

frame.columnconfigure(tuple(range(10)), weight=1)
frame.rowconfigure(tuple(range(5)), weight=1)

root.mainloop()