# # def summator(x=30, y=10):
# def summator(*args, **kwargs):
#     # x = 7
#     # y = 12
#     print(args)
#     print(kwargs)
#     # return x + y
#     return sum(args)
#
#
# n = summator(10, y=20)
# # print(n)
# print(summator(5, 7, 3, 5, 6))
# print(summator(15, 26))
# print(summator(5))
# print(summator())

# def summator():
#     x = input('rytrytruy ')
#     y = input('gyreyujhhkj ')
#     # print(x + y)
#     return x + y
#
# s = summator()
# print(s)

# def proba(x, y):
#     # x += 1  # локальная переменная
#
#     print('x =', x, y)
#
#
# x = 100  # глобальная
# proba(2, 77)
# print('Modul X =', x)


def proba(z, y):
    global x
    x += 50

    print('x =', x, y)


x = 100  # глобальная
proba(2, 77)
x = 300
proba(2, 77)
print('Modul X =', x)


def is_even(n: int = 5) -> bool:
    """Docstring."""
    # if n % 2 == 0:
    #     return True
    # else:
    #     return False
    return n % 2 == 0


def choice_even(x, y):
    for i in range(x, y + 1):
        if is_even(i):
            print(i, end=' ')


# choice_even(100, 141)

# print(is_even(12))
# is_even('12')
# print(is_even.__doc__)

# def num2(n):
#     if n > 1:
#         num1(n-1)
#     print(n)
#
# def num1(n):
#     if n > 1:
#         num2(n-1)
#     print(n)

def num(n):
    if n > 1:
        num(n - 1)
    print(n)


# num(5)

"""
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
n = n-1 + n-2
"""


def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# print(fib(5))

ls = [1, 2, [3, 4, [5, [6, 7], 8]]]

def smr(l):
    sm = 0
    for i in l:
        # if type(i) == int:
        if isinstance(i, int):
            sm += i
        else:
            sm += smr(i)
    return sm

# print(smr(ls))

def name(nm):
    cnt=0
    def surname(snm):
        nonlocal cnt
        cnt += 1
        print(cnt, nm, snm)
    return surname

cnt = 1000
sur = name('Mary')
sur('Petrova')
sur('Ivanova')
sur('Sidorova')