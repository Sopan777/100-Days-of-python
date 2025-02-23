import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

num = len(names) - 1

# card = random.choice(names)

card = random.randint(0, num)
print(f"{names[card]} is going to buy the meal today!")
# print(f"{card} is going to buy the meal today!")

