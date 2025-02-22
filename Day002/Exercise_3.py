# Calculating how many days weeks and years are left in owr life

age = input("Enter your current age: ")

year = 90 - int(age)
months = int(year)*12
days= int(year)*365
weeks = int(int(days)/7)

print(f"You have {days} days, {weeks} weeks, {months} months, {year} years")

