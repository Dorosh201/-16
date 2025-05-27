from tkinter import *

root = Tk()
canvas = Canvas(root, width=500, height=300, bg="skyblue")
canvas.pack()

# Земля
canvas.create_rectangle(0, 200, 500, 300, fill='green', outline='green')

# Будинок
canvas.create_rectangle(150, 150, 300, 250, fill='burlywood3')
canvas.create_polygon(135, 150, 225, 90, 315, 150, fill='sienna4')

# Двері
canvas.create_rectangle(210, 190, 240, 250, fill='peru')

# Вікна
canvas.create_rectangle(165, 170, 190, 195, fill='lightblue')
canvas.create_rectangle(260, 170, 285, 195, fill='lightblue')

# Дерево
canvas.create_rectangle(60, 170, 75, 230, fill='saddlebrown')
canvas.create_oval(40, 140, 95, 190, fill='forestgreen')

# Сонце
canvas.create_oval(400, 20, 460, 80, fill='yellow')

# Трава
for i in range(0, 500, 15):
    canvas.create_line(i, 200, i + 5, 190, fill='darkgreen')

root.mainloop()
