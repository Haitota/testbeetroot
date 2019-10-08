# С помощью random сгенерировать 2 целых числа и спросить у пользователя ответ суммы этих чисел.
# Если пользователь посчитал верно то засчитать ему одно очко. Повторять пока пользователь не введет ‘q’.
import random

count = 0
while True:
    a = random.randint(0, 20)
    b = random.randint(0, 20)
    sum_bot = a + b
    print("Count: ", count)
    answer = input('Sum: %s + %s = ?\n(If you want to quit, press q) ---> ' % (a, b))
    if answer == 'q':
        break
    elif int(answer) != sum_bot:
        print("The answer is not correct!")
        continue
    count += 1


