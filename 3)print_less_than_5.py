a = [1, 2, 3, 4, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5]
num = int(input("enter a numb"))
if num > 5:
    print(a)
if num <= 5:
    print(b)

c=list()
num = int(input('Give me a number: '))
for i in a:
    if i < num:
        c.append(i)
print(c)


