name = input("Enter your name: ")
age_str = input("Enter your age: ")
age = int(age_str)
current_year = 2026
years_until_100 = 100 - age
turn_100_year = current_year + years_until_100
print("Hello " + name + "!")
print("You will turn 100 in the year " + str(turn_100_year) + ".")
