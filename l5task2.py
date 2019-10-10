# Написать функцию, которая будет возвращать True если в списке,
# который передается функции как аргумент присутствует последовательность
# чисел 1, 2, 3, 4
LIST = set(map(int, input("Write a random list: ").split()))
print(type(LIST))


def s_s(a):
    if a.issuperset({1, 2, 3, 4}):
        print(True)
    else:
        print(False)


s_s(LIST)
