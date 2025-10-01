# file = open('text.txt', 'r', encoding='utf-8')
# # s = file.readline()
# # print(s)
# # s = file.read()
# # print('111', s)
# ls = file.readlines()
# print(ls)
# file.close()

# for i in open('text.txt', 'r', encoding='utf-8'):
#     print(i.strip())

with open('text.txt', 'r', encoding='utf-8') as fl:
    ls = fl.read().title().split()
ls.sort()
print(ls)

# with open('text1.txt', 'a', encoding='utf-8') as file:
with open('text1.txt', 'w', encoding='utf-8') as file:
    for k, i in enumerate(ls, 1):
        file.write(f'{k}. {i}\n')

#     ls = fl.readlines()
# print(ls)
# for i in ls:
#     word = i.split()
#     for j in word:
#         print(j)