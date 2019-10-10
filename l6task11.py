List = list(map(int, input("Write a list: ").split()))
print(List)
count = 0
for elem in List:
    if elem == 9:
        count += 1
print('Nine:', count)
