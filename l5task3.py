# Написать функцию, которая принимает список как аргумент и возвращает True
# если первый и последний элемент в списке равен 6
LIST = list(map(int, input("Write a random list: ").split()))
print(LIST)


def func_66(l):
    if l[0] == 6 and l[-1] == 6:
        print(True)
    else:
        print(False)


func_66(LIST)
