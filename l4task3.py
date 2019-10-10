import random
print('-----Game-----')
print('Stone/Scissors/Paper')
user_name = input("Please, insert your name:")
print('Greetings, ' + str(user_name))
gamer = str(input("Write your choice:"))


def game_ssp(g_r):
    op_g = ['Stone', 'Scissors', 'Paper']
    random.shuffle(op_g)
    bot = random.choice(op_g)
    print("Bot choice:", bot)
    if g_r == bot:
        print('Draw')
    elif g_r == 'Stone' and bot == 'Scissors':
        print('You win, well done!')
    elif g_r == 'Scissors' and bot == 'Paper':
        print('You win, well done!')
    elif g_r == 'Paper' and bot == 'Stone':
        print('You win, well done!')
    elif g_r == 'Scissors' and bot == 'Stone':
        print('You lose!')
    elif g_r == 'Paper' and bot == 'Scissors':
        print('You lose!')
    elif g_r == 'Stone' and bot == 'Paper':
        print('You lose!')
    else:
        print('Sorry, incorrect input, try again!')


print(game_ssp(gamer))
