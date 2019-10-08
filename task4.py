# Написать функцию, которая будет принимать пароль.
# Если в пароле есть 1 большая буква и хотя бы 5 цифр, и его длина не менее 10 символов вывести:
# “Your password is strong.” в противном случае “Your password is not strong enough.”
Pass = str(input("Please, enter your password:"))
print(Pass)


def password(data):

    
#    if not(len(data) < 10 or data.isdigit() or data.isalpha() or data.islower() or data.isupper()) and data.isalnum():
#       print("Your password is strong.")
#    else:
#        print("Your password is not strong enough")


print(password(Pass))

