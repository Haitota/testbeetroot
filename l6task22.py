# Вывести количество четный и нечетных елементов в рандомной последовательности.
import random
list1 = random.sample(range(30), 10)
print(list1)
i = 0
count_even = 0
count_odd = 0
while i < len(list1):
    if list1[i] % 2 == 0:
        count_even += 1
    else:
        count_odd += 1
    i += 1
print('Even:', count_even, ' ', 'Odd:', count_odd)
