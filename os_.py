import os
from tkinter import *
from tkinter import filedialog as fd

from datetime import datetime

# os.mkdir('new')
# ps = os.path.join('new', 'new1')
# print(os.path.abspath(ps))
# os.makedirs(r'D:\UNITS\Python\Units\group504\new\new1', exist_ok=True)
# # with open(r'D:\UNITS\Python\Units\group504\new\new1\t_new1.txt', 'w', encoding='utf-8') as f:
# #     f.write('print()')
# tm = os.path.getmtime(r'D:\UNITS\Python\Units\group504\new\t_new.txt')
# tm1 = os.path.getmtime(r'D:\UNITS\Python\Units\group504\new\new1\t_new1.txt')
# print(tm, tm1)
# print(datetime.fromtimestamp(tm).replace(microsecond=0),
#       datetime.fromtimestamp(tm1).replace(microsecond=0))
# print(os.path.exists(r'D:\UNITS\Python\Units\group504\new\new1\t_new2.txt'))

"""определение количества папок, файлов и общий размер файлов"""


def cnt_dir_file_size(target):
    size = 0
    cnt_folders = 0
    cnt_files = 0
    ps = os.path.join(target)
    p = os.path.abspath(ps)
    for i in os.listdir(p):
        ps = os.path.join(p, i)

        if os.path.isfile(ps):
            cnt_files += 1
            size += os.path.getsize(ps)
        else:
            cnt_folders += 1

            # size += cnt_dir_file_size(ps)[0]
            # cnt_folders += cnt_dir_file_size(ps)[1]
            # cnt_files += cnt_dir_file_size(ps)[2]
            sz, cf, cfl = cnt_dir_file_size(ps)
            size += sz
            cnt_folders += cf
            cnt_files += cfl
    return size, cnt_folders, cnt_files


root = Tk()

root.withdraw()

dir_ = fd.askdirectory()
if dir_:
    print(dir_)
    res = cnt_dir_file_size(dir_)
    # print(res)

wind = Tk()
answer = Text(wind)
answer.config(font=('Currier new', 20))
answer.pack(pady=15)
answer.insert(END, f'Размер файлов - {res[0]}\n')
answer.insert(END, f'Кол-во файлов - {res[2]}\n')
answer.insert(END, f'Кол-во папок  - {res[1]}\n')
wind.mainloop()
root.mainloop()
# print(cnt_dir_file_size('new'))
