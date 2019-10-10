num1 = 7
num2 = 1


def func_1(a, b):
    sum_1 = a + b
    if sum_1 > 10:
        print("This sum is greater than 10. It’s", sum_1)
    else:
        print("This sum is less than 10. It’s", sum_1)
    return sum_1


func_1(num1, num2)
