import random
from decorators import time_run, smr


@time_run
def left(l):
    temp = l[0]
    for i in range(len(l)-1):
        l[i] = l[i+1]
    l[-1] = temp
    return l


ls = list(range(1, 20000000))
print(__name__)
print(left(ls)[:10])

result = smr(random.randint(1, 100), random.randint(1, 200)) / .5 * 431
print(result)