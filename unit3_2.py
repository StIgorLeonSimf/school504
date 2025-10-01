import random

# ls = []
# for i in range(10, 20):
#     if i ** 2 % 2 == 0:
#         if i ** 2 < 200:
#             ls.append(i ** 2)
#         else:
#             ls.append(False)
# print(ls)
#
# ls1 = [i ** 2 if i ** 2 < 200 else True for i in range(10, 20) if i ** 2 % 2 != 0]
# print(ls1)

print(random.random())
print(random.uniform(-10, 0))

print(random.randint(11, 12))
print(random.randrange(10, 20, 2))

print(random.choice(range(10, 20, 3)))
ls = [22, 11, 55, 432, 123]
names = ['Lera', 'Mary', 'Alex', 'John', 'Helen']
print(random.choice(ls))
print(random.choice(names))

print(random.choices(names, k=7))
print(random.sample(names, 3))

print(ord('A'))
print(chr(67))
print(chr(128512))
for i in range(128512, 128535):
    print(f'Код: {i}  Символ: {chr(i)}')
print(ord('😄'))
