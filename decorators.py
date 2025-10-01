import random
import time


def decor(func):
    def wrapper():
        print('Before')
        func()
        print('After')
    return wrapper


def time_run(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        stop = time.perf_counter()
        duration = stop - start
        print(f'Функция {func.__name__} работает {duration:.2f} сек.')
        return res
    return wrapper


def in_out(func):
    def wrapper(*args, **kwargs):
        print(f'На входе функции {func.__name__} - {args}, {kwargs}')
        res = func(*args, **kwargs)
        print(f'На выходе функции {func.__name__} - {res}')
        return res
    return wrapper


@decor
def proba():
    print('PROBA')

@time_run
def etalon(n, m):
    print('START')
    time.sleep(n + m)

@in_out
def smr(x, y):
    return x + y

# print(__name__)
if __name__ == '__main__':
    pass
    # proba()
    # fn = decor(proba)
    # fn()
    # etalon(3, 1)
