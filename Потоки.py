# from threading import Thread
# import time
#
# from decorators import time_run
#
# @time_run
# def f1(x: int):
#     print(x ** 2)
#     time.sleep(3)
#     print(f'Фукция F1 работу закончила')
#
# @time_run
# def f2(x: int):
#     print(x * 2)
#     time.sleep(2)
#     print(f'Фукция F2 работу закончила')
#
#
# @time_run
# def main():
#     f1(3)
#     f2(3)
#
#
# # main()
# thread1 = Thread(target=f1, args=(3,), daemon=True)
# thread2 = Thread(target=f2, args=(5,))
#
# start = time.perf_counter()
# thread2.start()
# thread1.start()
# # thread1.join()
# # thread2.join()
# thread2.daemon = True
# stop = time.perf_counter()
# print(f'{stop - start:.2f} cек.')

l = [22, 33, 44, 55]
# temp = l[-1]
n = len(l)
# for i in range(n-2, -1, -1):
#     l[i + 1] = l[i]
# l[0] = temp
# for i in range(n-1, 0, -1):
#     l[i], l[i-1] = l[i-1], l[i]
# print(l)

def proba(n: int, m: int) -> int :
##    print('Proba', n, m)
    return n + m


xn = proba('12', '25')
print(xn)
xn = proba(10, 20)
print(xn)
xn = proba(122, 250)
print(xn)
