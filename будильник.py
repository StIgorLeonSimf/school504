from tkinter import *
from tkinter import messagebox
from time import strftime
import pygame as pg

pg.init()
pg.mixer.music.load('music.mp3')


def start():
    global alarm_time
    alarm_time = alarm.get().strip()
    messagebox.showinfo('Установка времени',
                        f'Будильник установлен на {alarm_time}'
                        )


def stop():
    global alarm_time
    alarm_time = ''
    alarm.delete(0, END)
    pg.mixer.music.stop()
    messagebox.showinfo('Предупреждение', f'Будильник отключен')


root = Tk()
root.geometry('450x250+400+200')
root.config(bg='black')
root.title('Будильник')

time = Label(root, text='00:00:00')
time.config(bg='black', fg='lime', font='Arial 50')
time.pack(pady=10)

alarm = Entry(root)
alarm.config(width=8, justify='center')
alarm['font'] = 'Arial 20'
alarm.pack()

btn_on = Button(root)
btn_on.config(text='Включить', width=10, font='Arial 12', command=start)
btn_on.pack(pady=10)

btn_off = Button(root)
btn_off.config(text='Выключить', width=10, font='Arial 12', command=stop)
btn_off.pack()

alarm_time = ''


def tick():
    global alarm_time
    # time_now = strftime('%H:%M:%S')
    time_now = strftime('%X')
    if (alarm_time == time_now or alarm_time == strftime('%H:%M')
            or alarm_time == strftime('%H')):
        alarm_time = ''
        pg.mixer.music.play()

    # time.config(text=time_now)
    time['text'] = time_now
    # tick()
    time.after(1000, tick)


tick()
root.mainloop()

d = {22: 2000, 33: 3000}
print(d.get(23, 'cвоё значение'))
