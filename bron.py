from tkinter import *
import json

# seats = {str(i): 'free' for i in range(1, 10)}
with open('text.txt', 'r') as fl:
    s = fl.read()
    print(s, type(s))
    seats = json.loads(s)
    print(seats)
c = 0
exit(0)


with open('seats.json', 'r') as fl:
    seats = json.load(fl)
    # json.dump(seats, fl)


#

# print(seats)


def handler(key):
    if seats.get(str(key)) == 'free':
        seats[str(key)] = 'busy'
        btns[key - 1].config(bg='yellow')
        with open('seats.json', 'w') as fl:
            json.dump(seats, fl)
    pass


def handler1(event, key):
    if seats.get(str(key)) == 'busy':
        seats[str(key)] = 'free'
        btns[key - 1].config(bg='lightgray')
        with open('seats.json', 'w') as fl:
            json.dump(seats, fl)


root = Tk()
root.geometry('300x300+450+200')
frame = Frame(root)
frame.pack(pady=10)

# btn1 = Button(frame)
# btn1.config(width=3, font='Arial 20 bold', text='1',
#             bg='lightgray' if seats['1'] == 'free' else 'yellow',
#             command=lambda: handler('1'))
# btn1.grid(row=0, column=0)
#
# btn2 = Button(frame)
# btn2.config(width=3, font='Arial 20 bold', text='2',
#             bg='lightgray' if seats['2'] == 'free' else 'yellow',
#             command=lambda: handler('2'))
# btn2.grid(row=0, column=1)
#
# btn3 = Button(frame)
# btn3.config(width=3, font='Arial 20 bold', text='3',
#             bg='lightgray' if seats['3'] == 'free' else 'yellow',
#             command=lambda: handler('3'))
# btn3.grid(row=0, column=2)
btns = []
for i in range(3):
    for j in range(3):
        num = i * 3 + j + 1
        btn = Button(frame)
        btn.config(width=3, font='Arial 20 bold', text=num,
                   command=lambda n=num: handler(n))
        btn.grid(row=i, column=j)
        btn.bind('<Button-3>', lambda event, n=num: handler1(event, n))
        btns.append(btn)

for k, v in seats.items():
    if v == 'busy':
        btns[int(k) - 1].config(bg='yellow')
    else:
        btns[int(k) - 1].config(bg='lightgrey')

root.mainloop()
