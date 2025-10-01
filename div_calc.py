import math
from tkinter import *


def add(n1, d1, n2, d2):
    if d1 != d2:
        n1 *= d2
        n2 *= d1
        n = n1 + n2
        d = d1 * d2
        return n, d
    else:
        d = d1
        n = n1 + n2
        return n, d


def sub(n1, d1, n2, d2):
    if d1 != d2:
        n1 *= d2
        n2 *= d1
        n = n1 - n2
        d = d1 * d2
        return n, d
    else:
        d = d1
        n = n1 - n2
        return n, d


def mult(n1, d1, n2, d2):
    n = n1 * n2
    d = d1 * d2
    return n, d


def div(n1, d1, n2, d2):
    n = n1 * d2
    d = d1 * n2
    return n, d


def main():
    operator = '+'
    try:
        n1 = int(num1.get())
        d1 = int(den1.get())
        n2 = int(num2.get())
        d2 = int(den2.get())
        operator = oper.get().strip()

    except Exception as er:
        print(er)
        n1, d1, n2, d2 = 1


    if operator == '+':
        res = add(n1, d1, n2, d2)
    elif operator == '-':
        res = sub(n1, d1, n2, d2)
    elif operator == '*':
        res = mult(n1, d1, n2, d2)
    elif operator == '/':
        res = div(n1, d1, n2, d2)

    nod = math.gcd(res[0], res[1])
    n = res[0] / nod
    d = res[1] / nod
    integ = '   '
    if n > d:
        integ = n // d
        n = n % d
    if integ != '   ':
        intr.config(text=int(integ))
    if n == 0 or n == d:
        numr['text'] = '   '
        denr.config(text='   ')
        if integ != '   ':
            intr.config(text=1)
    else:
        numr['text'] = int(n)
        denr.config(text=int(d))


root = Tk()
root.geometry('400x180+425+200')
root.title('Калькулятор дробей')
frame = Frame(root)
frame.pack(pady=10)

num1 = Entry(frame)
num1.config(width=3, font='Arial 20', justify='center')
num1.grid(row=0, column=0)

line1 = Label(frame, text='-----------')
line1.grid(row=1, column=0)

den1 = Entry(frame, width=3, font='Arial 20', justify='center')
# den1.config(width=3, font='Arial 20')
den1.grid(row=3, column=0)

oper = Entry(frame, width=1, font='Arial 20')
oper.grid(row=1, column=1, padx=10)

num2 = Entry(frame)
num2.config(width=3, font='Arial 20', justify='center')
num2.grid(row=0, column=2)

line2 = Label(frame, text='-----------')
line2.grid(row=1, column=2)

den2 = Entry(frame)
den2.config(width=3, font='Arial 20', justify='center')
den2.grid(row=3, column=2)

make = Button(frame)
make.config(font='Arial 10', width=3, text='=', command=main)
make.grid(row=1, column=3, padx=10)

intr = Label(frame)
intr.config(text='   ', bg='lightgray', font='Arial 30', justify='center')
intr.grid(row=1, column=4)

numr = Label(frame)
numr.config(width=3, font='Arial 20', bg='lightgray', justify='center')
numr.grid(row=0, column=5)

liner = Label(frame, text='-----------')
liner.grid(row=1, column=5)

denr = Label(frame)
denr.config(width=3, font='Arial 20', bg='lightgray', justify='center')
denr.grid(row=3, column=5)

root.mainloop()
