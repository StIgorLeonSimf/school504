import asyncio
import os.path

from g4f.client import AsyncClient
# from g4f.Provider import OpenaiChat
import requests
from io import BytesIO
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog

from translate import Translator



async def generate_image_url():
    global name
    client = AsyncClient()
    response = await client.images.generate(
        # prompt="kittes",
        prompt=nm,
        model="imagen-4",
        response_format="url"

    )

    image_url = response.data[0].url
    print(f"Generated image URL: {image_url}")

    return image_url


def load_image(url):
    global img_s
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        image_data = BytesIO(resp.content)
        img_s = Image.open(image_data)
        # img_s.thumbnail((850, 650))
        return ImageTk.PhotoImage(img_s)
    except Exception as er:
        img_s = None
        print(f'Error loading image - {er}')
    return None


def run_mode():
    global img, nm
    nm = name.get().strip()
    nm = translator.translate(nm.capitalize())
    print(nm)
    url = asyncio.run(generate_image_url())
    if url:
        img = load_image(url)

    if img:
        label.config(image=img)
        label.image = img


def path_name(event):
    nm_f = name_file.get().strip()
    return nm_f


def save_picture():
    global img_s
    if img_s is None:
        print("No image to save")
        return

    default_name = os.path.basename(name_file)
    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png"), ("All files", "*.*")],
        initialfile=default_name
    )
    if file_path:
        img_s.save(file_path)
        print(f"Image saved to {file_path}")


if __name__ == "__main__":
    name_file = 'Picture.png'
    img_s = None
    translator = Translator(from_lang='ru', to_lang='en')
    root = tk.Tk()
    root.title('Cats')
    root.geometry('850x650')
    frame1 = tk.Frame(root)
    frame1.pack(pady=10)
    frame2 = tk.Frame()
    frame2.pack()
    name = tk.Entry(frame1, width=50, font='Arial 15')
    name.insert(0, 'kittens')
    name.grid(row=0, columnspan=2, pady=5)
    nm = name.get().strip()
    btn = tk.Button(frame1)
    btn.config(text='Forward', width=10, command=run_mode)
    btn.grid(row=1, column=0)
    btn_s = tk.Button(frame1, text='Save', width=10, command=save_picture)
    btn_s.grid(row=1, column=1)
    label = tk.Label(frame2)
    label.pack(pady=10)
    url = asyncio.run(generate_image_url())
    if url:
        img = load_image(url)

    if img:
        label.config(image=img)
        label.image = img

    root.mainloop()
