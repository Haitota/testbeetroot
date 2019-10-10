# Написать функцию, которая принимает 2 списка и возвращает True,
# если первые или последние элементы списка равны
List1 = list(map(int, input("Write a first random list: ").split()))
print(List1)
List2 = list(map(int, input("Write a second random list: ").split()))
print(List2)


def func_12(l1, l2):

    if l1[0] == l2[0] and l1[-1] == l2[-1]:
        print(True)
    else:
        print(False)


func_12(List1, List2)