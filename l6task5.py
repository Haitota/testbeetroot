# Посчитать факториал для введенного пользователем числа.
n = int(input('Enter factorial:'))
factorial = 1
while n > 1:
    factorial *= n
    n -= 1

print(factorial)

n_f = int(input('Enter factorial:'))
factorial = 1
for i in range(2, n_f + 1):
    factorial *= i

print(factorial)
