import time

import asyncio


# def f1(x:int):
#     print(x ** 2)
#     time.sleep(3)
#     print(f'Фукция F1 работу закончила')
#
#
# def f2(x:int):
#     print(x * 2)
#     time.sleep(3)
#     print(f'Фукция F2 работу закончила')
#
# def main():
#     f1(3)
#     f2(3)
#
#
# if __name__ == '__main__':
#     start = time.perf_counter()
#     main()
#     stop = time.perf_counter()
#     print(f'{stop - start:.2f} cек.')


async def f1(x: int):
    print(x ** 2)
    await asyncio.sleep(3)
    print(f'Фукция F1 работу закончила')


async def f2(x: int):
    print(x + 2)
    await asyncio.sleep(3)
    print(f'Фукция F2 работу закончила')


async def main():
    # task1 = asyncio.create_task(f1(3))
    # task2 = asyncio.create_task(f2(3))
    # task1
    # await task2
    await asyncio.gather(f1(4), f2(25))


if __name__ == '__main__':
    start = time.perf_counter()
    asyncio.run(main())
    stop = time.perf_counter()
    print(f'{stop - start:.2f} cек.')