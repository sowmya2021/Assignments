number = input("Enter a number: ")
if int(number) % 2 == 0:
    print(number," is an Even number.")
else:
    print(number," is an Odd number.")
if int(number) % 4 == 0:
    print(number," is a multiple of 4")
num = input("Enter first number: ")
check = input("Enter 2nd Number: ")
if int(num) % int(check) == 0:
    print(num," divides evenly by ",check)
else:
    print(num, " does NOT divide evenly by " ,check)
