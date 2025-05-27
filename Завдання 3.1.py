import tkinter as tk

root = tk.Tk()
root.title("коло і квадрат")

canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

canvas.create_oval(200, 50, 300, 150, fill="red", outline="black", width=2)
canvas.create_rectangle(50, 50, 150, 150, fill="yellow", outline="black", width=2)

root.mainloop()