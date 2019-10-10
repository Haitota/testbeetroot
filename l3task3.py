temp_re = int(input("Enter temperature: "))


def sq(t, is_summer):
    if 60 <= t <= 90 and not is_summer:
        print('It is not summer. Playing')
    elif 60 <= t <= 100 and is_summer:
        print("It is summer. Playing")
    else:
        print("Not Playing")


sq(temp_re, True)