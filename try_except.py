# try:
#     n = int(input('> '))
# except ValueError:
#     print('no digit!!!')
# except TypeError as er:
#     print('no type!!!', er)
# else:
#     print(n)
# finally:
#     print('Всегда')

# try:
#     file = open('text2.txt', 'r', encoding='utf-8')
#     s = file.read()
# except Exception as err:
#     print('Oшибка', err)
# finally:
#     file.close()
file = open('text.txt', 'r', encoding='utf-8')
s = file.read()