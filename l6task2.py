# Вывести количество четный и нечетных елементов в рандомной последовательности.
import random
list1 = random.sample(range(30), 10)
print(list1)
count_even = 0
count_odd = 0
for elem in list1:
    if elem % 2 == 0:
        count_even += 1
    else:
        count_odd += 1

print('Even:', count_even, ' ', 'Odd:', count_odd)
