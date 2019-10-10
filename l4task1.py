#Напишите программу, которая генерирует случайное число от 1 до 10 и позволяет пользователю угадать,
#какое число было сгенерировано.
#Результат должен быть отправлен обратно пользователю с помощью оператора печати.
import random


print('-----The Guessing Game-----')
gamer = int(input("Guess a random number between 1 and 10: "))


def game_gg(g_r):
    bot = random.randint(0, 10)
    print("Bot number:", bot)
    if g_r == bot:
        print('You win, well done!')
    else:
        print('You lose!')


game_gg(gamer)
