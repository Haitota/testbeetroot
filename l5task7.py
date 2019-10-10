# Определить самый большой элемент списка и заменить им все элементы.
# Длина списка не больше 5
List = list(map(int, input("List length not more than 5! Write a list: ").split()))
print(List)
l_l = len(List)
print('List length:', l_l)
if l_l <= 5:
    def sum_max(l):
        z = [max(l) for i in l]
        return z
    print(sum_max(List))
else:
    print('List length is greater than 5')
