""" словари (dict)"""
#
# # d = {}
d = {'Pb': 'свинец',
     'Au': 'Золото'
     }

print(d['Pb'])
print(d.get('Pb1', 'свое значение'))

d['Pb'] = 'Свинец'

d[1] = 111
print(d.setdefault(2, 22))
d.update({3: 33, 1: 11})

n = d.pop(2)
n1 = d.popitem()
print('delete', n, n1)
print(d)

# l = [22, 33, 22]
# # dd = dict.fromkeys(l, [])
# # dd[22].append(20)
# dd = {i: [] for i in l}
# dd[22].append(20)
# print(dd)

# ls = [('Mary', 22), ('Pit', 33), ('Nataly', 44)]
# dd = dict(ls)

# print(dd)
# dd = {}
# for i in range(10, 20):
#      dd[i] = i ** 2
# print(dd)
#
# dd = {i: i ** 2 for i in range(10, 20)}
# print(dd)
# print(d.keys())
# print(list(d))
# print(list(d.values()))
# print(list(d.items()))
#
# for k in d:
#     print(k, end=' ')
# print()
# for v in d.values():
#     print(v, end=' ')
# print()
# for k, v in d.items():
#     print(k, v, end='     ')
# print()
#
# for k in d.items():
#     print(k[0], k[1], end='     ')
# print()
#
# for k in d:
#     print(k, d[k], end='     ')
# print()


ls = [('Mary', [22, 'student']), ('Pitergoff', [33, 'ticher']), ('Nataly', [44, 'admin'])]
dd = dict(ls)
# print(dd)
for k, v in dd.items():
     print(f'Имя: {k:6}, Возраст {v[0]} года, Профессия: {v[1]}.')

# max_k = max(dd, key=lambda x: len(x))
# mx = len(max_k)
# # print(max_k)
# print(mx)
# for k, v in dd.items():
#      print(f'Имя: {k:{mx}}, Возраст {v[0]} года, Профессия: {v[1]}.')