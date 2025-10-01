from functools import reduce

l = [22, 33, 44]
l1 = [1, 2, 3, 4, 5]


# res = list(map(str, l))
# for i in res:
#     print('1', i)
# for i in res:
#     print('2', i)
# print('end')
def power(n):
    return n ** 2


# res = list(map(power, l))
# res = list(map(lambda n: n ** 2, l))
# print(res)
# print((lambda x: x ** 3)(3))

res = list(map(lambda n, m: n - m, l, l1))
res = list(map(lambda n, m: n > m, l, l1))
print(res)

res = list(filter(lambda x: x % 2 == 0, l))
res1 = [i for i in l if i % 2 == 0]
res2 = []
cnt = 0
for i in l:
    cnt += 1
    if i == 22:
        res2.append(i)
        break
print(res)
print(res1)
print(res2, cnt)

city = ['У', 'ф', 'а', '-', 4, 5]

# res = reduce(lambda n, m: str(m) + str(n), city)
res = reduce(lambda n, m: m * n, l1)
print(res)
