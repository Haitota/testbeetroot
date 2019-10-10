# Написать функцию, которая будет принимать пароль.
# Если в пароле есть 1 большая буква и хотя бы 5 цифр, и его длина не менее 10 символов вывести:
# “Your password is strong.” в противном случае “0”


def p():
    while True:
        password = input("Please, enter your password:")
        if len(password) < 10:
            print("Your password is not strong enough. Make sure your password is at lest 10 letters!")
        for elem in password:
            if not (elem.isdigit()) == 5:
                print("Your password is not strong enough. Make sure your password has a number in the password")
        if not any([x.isupper() for x in password]):
            print("Your password is not strong enough. Make sure your password has one capital letter in the password")
        else:
            print("Your password is strong!")
            break

p()

