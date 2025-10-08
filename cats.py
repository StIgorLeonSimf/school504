from tkinter import *

import requests
from PIL import Image, ImageTk
from io import BytesIO


# URL = 'https://cataas.com/cat/little,cute'
URL = 'https://source.unsplash.com/category/food'


def text(txt):
    global URL
    URL = f'https://cataas.com/cat/{txt}'
    wind.destroy()


def load_image(url):
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        data = BytesIO(resp.content)
        img = Image.open(data)
        return ImageTk.PhotoImage(img)
    except Exception as err:
        print('Ошибка', err)
        return None


def new_img():
    img = load_image(URL)
    if img:
        pict.config(image=img)
        pict.image = img


wind = Tk()
btn1 = Button(wind, text='little,cute',
              command=lambda: text('small'))
btn1.pack(pady=10)
btn2 = Button(wind, text='brown',
              command=lambda: text('brown'))
btn2.pack()
wind.mainloop()
root = Tk()
root.title('Котики')
WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()
WIDTH_R = 600
HEIGHT_R = 500
root.geometry(f'{WIDTH_R}x{HEIGHT_R}+'
              f'{WIDTH//2 - WIDTH_R//2}+{HEIGHT//2 - HEIGHT_R//2}')

btn = Button(root, width=10, text='New', command=new_img)
btn.pack(pady=10)
pict = Label(root)
pict.pack()

img = load_image(URL)
if img:
    pict.config(image=img)
#     # pict.image = img


root.mainloop()