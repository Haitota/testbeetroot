# Написать функцию, которая принимает список как аргумент и возвращает True если цифры 2 и 3 есть в этом списке
L = list(map(int, input("Write a random list: ").split()))
print(L)


def func_23(l):
    if 2 in l and 3 in l:
        return True
    else:
        return False


print(func_23(L))
