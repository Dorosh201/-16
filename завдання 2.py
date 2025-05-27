from tkinter import *
import time

root = Tk()
root.title("Анімація: машини")
canvas = Canvas(root, height=600, width=1000, bg='white')
canvas.pack()

car_1_img = PhotoImage(file="1.png")
car_2_img = PhotoImage(file="2.png")

# Додаємо машинку_1 на полотно
car_1 = canvas.create_image(10, 110, image=car_1_img, anchor=NW)
canvas.image = car_1_img  # щоб зображення не зникло

# Машинка 1 їде
for i in range(1, 100):
    canvas.move(car_1, 10, 0)
    root.update()
    time.sleep(0.01)

# Додаємо машинку_2 на полотно 
car_2 = canvas.create_image(10, 100, image=car_2_img, anchor=NW)
canvas.image2 = car_2_img  # щоб зображення не зникло

# Машинка 2 їде 
for i in range(1, 100):
    canvas.move(car_2, 10, 0)
    root.update()
    time.sleep(0.01)

root.mainloop()
