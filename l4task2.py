#Напишите программу, которая принимает ваше имя в качестве входных данных,
#а затем ваш возраст в качестве входных данных и приветствует вас следующим:
#“Hello <name>, on your next birthday you’ll be <age+1> years”

name = str(input("Please, insert your name:"))
age = int(input("Please, insert your age:"))


def greeting_program(name_, age_u):
    age_u += 1
    text_ = 'Hello %s, on your next birthday you’ll be %d years' % (name_, age_u)
    return text_


print(greeting_program(name, age))

