# Дано 2 списка int, a и b, длина каждого равна 3.
# Написать функцию, которая принимает оба списка и возвращает новый список длиной 2,
# содержащий их средние элементы.
a = [1, 7, 12]
b = [6, 12, 3]


def list_2(l1, l2):
    elem1 = l1[1]
    elem2 = l2[1]
    print(list([elem1, elem2]))


list_2(a, b)
