from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO


def load_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = BytesIO(response.content)
        img = Image.open(image_data)
        img.thumbnail((600, 480), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Ошибка при загрузке изображения: {e}")
        return None


def set_image():
    img = load_image(url)

    if img:
        label.config(image=img)
        label.image = img  # Сохраняем ссылку на изображение

def exit():
    window.destroy()

window = Tk()
window.title("Cats!")
window.geometry("600x520")
label = Label(window)
label.pack()


def exit():
    window.destroy()


window = Tk()
window.title("Cats!")
window.geometry("600x520")
label = Label(window)
label.pack()

# Создаем меню
menu_bar = Menu(window)
window.config(menu=menu_bar)

# Добавляем пункты меню
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Загрузить фото", command=set_image)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=exit)

url = 'https://cataas.com/cat/cute'
set_image()

window.mainloop()
