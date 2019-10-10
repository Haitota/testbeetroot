# Вывести последовательность Коллатца для числа введенного пользователем.
# Остановится когда число достигнет 1.
n_user = int(input('Please, enter your n: '))
print(n_user)


def col(n):
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        print(n)


col(n_user)

