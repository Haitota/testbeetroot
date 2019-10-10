# Написать функцию, которая принимает 3 списка
# и возвращает их общую сумму элементов
List1 = list(map(int, input("Write a first list: ").split()))
print(List1)
List2 = list(map(int, input("Write a second list: ").split()))
print(List2)
List3 = list(map(int, input("Write a third list: ").split()))
print(List3)


def func_123(l1, l2, l3):
    sum_3 = sum(l1) + sum(l2) + sum(l3)
    return sum_3


print(func_123(List1, List2, List3))
