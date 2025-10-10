# def interval(h):
#     if h >= 4 and h < 12:
#         print('Morning')
#     elif h >= 12 and h < 17:
#         print('DAY')
#     elif h >= 17 and h < 24:
#         print('Evening')
#     elif h >= 0 and h < 4 or h == 24:
#         print('Night')
#     else:
#         print('Нет такого времени!')
#
#
# while True:
#     try:
#         hh = float(input('Введите время суток: '))
#         interval(hh)
#     except Exception as er:
#         print(er)
#         break
import json
from tkinter import *

ROW = 10
COLUMN = 20
# tickets = {}
# for i in range(ROW):
#     for j in range(COLUMN):
#         tickets[i] = [{'column': j, 'status': 'free'} for j in range(COLUMN)]
# # tickets = {(i, j): 'free' for i in range(ROW) for j in range(COLUMN)}
# print(tickets)
# with open('tickets.json', 'w') as file:
#     json.dump(tickets, file)
with open('tickets.json', 'r') as file:
    tickets = json.load(file)

def handler(r, c):
    tickets[str(r)][c]['status'] ='busy'
    with open('tickets.json', 'w') as file:
        json.dump(tickets, file)
    btns[r][c].config(bg='lightgray')


def chandler_free(event, r, c):
    tickets[str(r)][c]['status'] = 'free'
    with open('tickets.json', 'w') as file:
        json.dump(tickets, file)
    if 0 <= r < 3:
        color = 'red'
    elif 3 <= r < 6:
        color = 'green'
    elif 6 <= r < 8:
        color = 'blue'
    else:
        color = 'yellow'

    btns[r][c].config(bg=color)

root = Tk()
root.title('Зал')
WIDTH = 1366
HEIGHT = 768
WIDTH_R = 800
HEIGHT_R = 400
root.geometry(f'{WIDTH_R}x{HEIGHT_R}+'
              f'{WIDTH//2 - WIDTH_R//2}+{HEIGHT//2 - HEIGHT_R//2 - 25}')

frame1 = Frame(root, width=580, height=40)
frame1.pack()
canvas = Canvas(frame1, width=480, height=40)
canvas.pack(pady=10)
canvas.create_line(10, 5, 570, 5, width=10, fill='grey')
canvas.create_line(10, 20, 70, 20, width=6, fill='#FF0000')
canvas.create_text(40, 30, text=600)
canvas.create_line(100, 20, 170, 20, width=6, fill='#00FF00')
canvas.create_text(135, 30, text=500)
canvas.create_line(200, 20, 270, 20, width=6, fill='#0000ff')
canvas.create_text(235, 30, text=400)
canvas.create_line(300, 20, 370, 20, width=6, fill='#FFFF00')
canvas.create_text(335, 30, text=300)

frame2 = Frame(root)
frame2.pack()


btns = []
for i in range(ROW):
    btns.append([])
    ln = Label(frame2, text=f'Ряд - {i+1}')
    ln.grid(row=i, column=0 )
    for j in range(COLUMN):
        if tickets[str(i)][j]['status'] == 'busy':
            color = 'lightgrey'
        elif 0 <= i < 3:
            color = 'red'
        elif 3 <= i < 6:
            color = 'green'
        elif 6 <= i < 8:
            color = 'blue'
        else:
            color = 'yellow'

        btn = Button(frame2, width=2, font='Arial 10', text=j+1, bg=color,
                     command=lambda r=i, c=j: handler(r, c))
        btn.grid(row=i, column=j+1)
        btns[i].append(btn)

for n, i in enumerate(btns):
    for m, j in enumerate(i):
        j.bind('<Button-3>', lambda event, r=n, c=m: chandler_free(event, r, c))
root.mainloop()