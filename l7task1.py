# Подсчитать количество каждого элемента в списке. Результат в виде словаря
list_1 = list(map(int, input("Write a random list: ").split()))
print(list_1)
d = {}
for elem in list_1:
    if elem in d:
        d[elem] = d[elem] + 1
    else:
        d[elem] = 1
print(d)
