# Дан список чисел L. Написать функцию, которая вернет True если сумма
# первых 4 элементов списка равны 9.
# При этом функция должна вызываться только если длина списка больше 4.
LIST = list(map(int, input("Write a random list: ").split()))
print(LIST)
l_l = len(LIST)
print('List length:', l_l)
if l_l > 4:
    def sum_f(l):
        sum_l = sum(l[0:4])
        if sum_l == 9:
            print('The sum of the first 4 elements of the list is 9')
        else:
            print('The sum of the first 4 elements of the list is NOT 9')
    sum_f(LIST)
    print(True)
else:
    print(False)
