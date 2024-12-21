first = int(input('введите1: '))
second = int(input('введите2: '))
third = int(input('введите3: '))
print(first,second,third)
if first == second and second == third:
    print(3)
elif first != second and second != third and first != third:
    print(0)
else:
    print(2)

