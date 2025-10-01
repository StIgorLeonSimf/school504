"""множества (set)"""

# l = [2, 3, 2, 3]
# st = set(l)
# print(st)

# st = {22, 33, 44}
#
# st.add(100)
# st.update({1, 2, 3})
# # st.update([11, 12, 13])
# # st.update((21, 32, 32))
#
# n = st.pop()
# st.remove(2)
# st.discard(1)
# print(n)
# print(st)
#
# st1 = {1, 2, 33}
# st2 = {1, 2, 44}

# res = st1.union(st2)  # объединение
# res = st1 | st2

# res = st1.intersection(st2)  # пересечение
# res = st1 & st2

# res = st1.difference(st2)  # вычитание
# res = st2 - st1

# res = st1.symmetric_difference(st2)
# res = st1 ^ st2
# print(res)
#
# st1 = {1, 2, 33}
# st2 = {1, 2, 44}
# st3 = {1, 2}
#
# print(st1.issuperset(st3))
# print(st3.issubset(st2))

# """ словари (dict)"""
#
# # d = {}
# d = {'Pb': 'свинец',
#      'Au': 'Золото'
#      }
#
# print(d['Pb'])
# print(d.get('Pb1', 'свое значение'))
#
# d['Pb'] = 'Свинец'
#
# d[1] = 111
# print(d.setdefault(2, 22))
# d.update({3: 33, 1: 11})
# print(d)


"""datetime"""

from datetime import datetime, date, time, timedelta

d = date(2025, 12, 31)
print(d, type(d))
t = time(12, 10, 4)
print(t, type(t))
dt = datetime.combine(d, t)
print(dt, type(dt))
print(date.today().year)
print(date.today().day)
print(date.today().month)
dtn = datetime.now()
print(dtn)
dtm = datetime.utcnow()
print(dtm)
print(dtn.strftime('%A %d %B %y  %I:%M %p'))
print(dtn.strftime('%d.%m.%Y  %H:%M:%S'))
print(dtn.strftime('%d.%m.%Y  %X'))
tp = dtn.timetuple()
# for i in tp:
#     print(i)
# calend = dtn.isocalendar()
# for i in calend:
#     print(i)
# print(dtn.weekday())
# print(dtn.isoweekday())
""" кол-во дней до ДР """
bd = input('Введите дату рождения (дд.мм.гггг): ')
bd = datetime.strptime(bd, '%d.%m.%Y').date()
print(bd)
year_ = date.today().year
dn = date.today()
bdy = bd.replace(year=year_)
if dn > bdy:
    bdy = bd.replace(year=year_ + 1)
cnt_d = bdy - dn
print(cnt_d.days)
