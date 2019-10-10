# Вывести последовательность Фибоначчи, где количество элементов последовательности задается пользователем
n = int(input('Please, enter your n for the Fibonacci Sequence: '))
fib1 = 0
print(fib1)
fib2 = 1
print(fib2)
i = 0
while i < n - 2:  # если поставить -1, то будет выдавать на одно число больше
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i = i + 1
    print(fib2)


