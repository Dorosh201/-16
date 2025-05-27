from tkinter import *
import winsound

# Обробники кліку 
def click_room(event):
    label.config(text="Living room — Вітальня],p;")
    winsound.PlaySound("Living room.wav", winsound.SND_FILENAME | winsound.SND_ASYNC) #Асинхронне відтворення звуку

def click_window(event):
    label.config(text="Window — Вікно")
    winsound.PlaySound("window_converted.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

def click_drape(event):
    label.config(text="Drape — Штора")
    winsound.PlaySound("Drape.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

root = Tk()
root.title("Вивчаємо англійську: Предмети із класної кімнати")
root.geometry("800x500")

canvas = Canvas(root, width=800, height=400, bg="white")
canvas.pack()

#Підпис під полотном 
label = Label(root, text="", font=("Arial", 20))
label.pack(pady=10)

room_img = PhotoImage(file="Зала.png")
window_img = PhotoImage(file="Вікно.png")
drape_img = PhotoImage(file="Штори.png")

#Виведення зображень
room_id = canvas.create_image(150, 200, image=room_img)
window_id = canvas.create_image(400, 200, image=window_img)
drape_id = canvas.create_image(650, 200, image=drape_img)

# Прив'язка кліків
canvas.tag_bind(room_id, "<Button-1>", click_room)
canvas.tag_bind(window_id, "<Button-1>", click_window)
canvas.tag_bind(drape_id, "<Button-1>", click_drape)

root.mainloop()
