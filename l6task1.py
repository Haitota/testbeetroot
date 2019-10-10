# Посчитать количество 9 в списке.
List = list(map(int, input("Write a list: ").split()))
print(List)
i = 0
count = 0
while i < len(List):
    if List[i] == 9:
        count += 1
    i += 1
print(count)

