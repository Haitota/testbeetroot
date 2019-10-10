import random

l1 = [random.randint(0, 10) for i in range(10)]
print(l1)
l2 = [random.randint(0, 10) for i in range(10)]
print(l2)
l3 = l1 + l2
print(set(l3))
