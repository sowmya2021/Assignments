list = []
number = int(input("Enter a number to find its divisor"))
for element in range((number - (number - 2)), (number - 1)):
    if number % element == 0:
        divide = int(number / element)
        list.append(element)
print(list)