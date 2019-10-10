print('17-12+9?')
user_q = int(input("Write your answer:"))


def math_quiz(ans):
    if ans != 14:
        print("You are mistaken!")
    else:
        print("Your answer is correct:", ans)


print(math_quiz(user_q))
