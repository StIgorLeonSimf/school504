with open('text1.txt', encoding='utf-8') as fl:
    s = fl.read()

key = input('Введите ключ шифрования:  ')
secret = ''
for i in s:
    code = ord(i) + int(key)
    symbol = chr(code)
    secret += symbol
print('Текст зашифрован')

with open('code.txt', 'w', encoding='utf-8') as fl:
    fl.write(secret)
print('Файл "code.txt" к отправке готов!')


