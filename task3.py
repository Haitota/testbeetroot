# Пользователь должен ввести последовательность чисел через пробел.
# Для каждого числа выведите слово YES (в отдельной строке),
# если это число ранее встречалось в последовательности или NO, если не встречалось.
List = list(map(int, input("Write a list: ").split()))
print(List)
s = set()
for elem in List:
    if elem in s:
        print('Yes')
    else:
        print('No')
        s.add(elem)
