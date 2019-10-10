# Вывести количество четный и нечетных елементов в рандомной последовательности.
# Результат в виде словаря
import random
list1 = random.sample(range(1, 30), 10)
print(list1)
d = {'even': 0, 'odd': 0}
for elem in list1:
    if elem % 2 == 0:
        d['even'] += 1
    else:
        d['odd'] += 1
print(d)
