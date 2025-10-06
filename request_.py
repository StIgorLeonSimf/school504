"""Напишите функцию`get_main()`, которая принимает
на вход ссылку на страницу сотрудника кафедры высшей математики
и возвращает кортеж из двух значений:

*строка с ФИО без постронних символов;
*строка с названием должности без постронних символов.

** Пример работы программы **

Запуск функции:

get_main("https://www.hse.ru/staff/allat")

Результат:

('Тамбовцева Алла Андреевна', 'Преподаватель')

Запуск функции:

get_main("https://www.hse.ru/org/persons/135897")

Результат:
('Макаров Алексей Алексеевич', 'Профессор')

Запуск функции:

get_main("https://www.hse.ru/org/persons/63890353")

Результат:

('Филимонов Дмитрий Андреевич', 'Доцент')"""
import requests
from bs4 import BeautifulSoup


def get_main(url):
    responce = requests.get(url)
    resp = BeautifulSoup(responce.text, 'html.parser')
    fio = resp.find('h1', class_='person-caption').text
    pos = resp.find('span', class_="person-appointment-title").text.strip()[:-1]
    answer = (fio, pos)
    lang = resp.find('dt', class_='b').find_all()
    print(answer)
    long = len('Владение языками')
    print(resp.find('dt', class_='b').text[:long] + ':')
    for i in lang:
        print(i.text)


get_main("https://www.hse.ru/staff/allat")
get_main("https://www.hse.ru/org/persons/135897")
get_main("https://www.hse.ru/org/persons/63890353")
