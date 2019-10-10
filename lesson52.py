import random
l1 = [random.randint(0, 10) for i in range(10)]
print(l1)

l_1 = list(range(1, 101))


def func5_7(item):
    if item % 7 == 0 and item % 5 != 0:
        return item


print(list(map(func5_7, l_1)))