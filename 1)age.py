import datetime
name = input("Enter your name as in Adhaar Card")
birth_year = int(input("Enter your year of birth:"))
current_year = datetime.date.today().year
age_year = current_year - birth_year
old_age = birth_year + 100
print("Hai",name)
print("Your age as of 2021: ", age_year)
print("The year you turn 100 years old is",old_age)