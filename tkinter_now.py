from tkinter import *


def result1(event):

    print(event.x, event.y)



def result():

    answ = int(n.get().strip())
    answ1 = int(n1.get().strip())
    res = answ + answ1
    answer.config(text=res)
# n = input('> ')
# print(n)
WIDTH = 1366
HEIGHT = 768
WIDTH_R = 450
HEIGHT_R = 250

root = Tk()
# root.geometry('450x250+400+200')
root.geometry(f'{WIDTH_R}x{HEIGHT_R}+'
              f'{WIDTH//2 - WIDTH_R//2}+{HEIGHT//2 - HEIGHT_R//2 - 25}')
text = Label(root, text='Введите значение:')
# text.config(font='Arial 20',  fg='#ffff00')
text.config(font='Arial 20')
text.pack(pady=10)
n = Entry(width=5, font='Arial 20', justify='center')
n.pack()
btn = Button(root)
btn.config(width=1, font='Arial 20', text='+', command=result)
btn.pack()
n1 = Entry(width=5, font='Arial 20', justify='center')
n1.pack()

answer = Label(root, text='        ')
answer.config(font='Arial 20')
answer.pack(pady=10)



# n1.bind('<Return>', result1)
# n1.bind('<Button-1>', result1)
root.mainloop()