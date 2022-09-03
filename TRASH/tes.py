from tkinter import Tk, Canvas
root = Tk()
canvas = Canvas()
canvas.grid()
canvas.create_text((10, 5), text="\n".join("This is some text"), anchor="nw")
root.mainloop()