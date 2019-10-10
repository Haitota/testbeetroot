# Написать функцию, которая вернет сумму первых 2 элементов в списке.
# Если длина списка меньше 2, просто суммируйте существующие элементы,
# возвращая 0, если массив имеет длину 0.
LIST = list(map(int, input("Write a random list: ").split()))
print(LIST)


def sum_f(l):
    l_l = len(l)
    if l_l < 2:
        return l[0]
    elif l_l > 2:
        return l[0] + l[1]
    else:
        return 0


print(sum_f(LIST))
