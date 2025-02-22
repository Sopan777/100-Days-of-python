# 🚨 Don't change the code below 
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0
# 🚨 Don't change the code above 👆

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "M":
    bill += 25
else:
    print("Invalid Input for Size of Pizza")

if add_pepperoni == "Y":
    if size == "S":
        bill +=2
    elif size == "L" or size == "M":
        bill +=3
elif add_pepperoni =="N":
    bill += 0
else:
    print("Invalid Input for Pepperoni")

if extra_cheese == "Y":
    if size == "S":
        bill += 1
elif extra_cheese =="N":
    bill += 0
else:
    print("Invalid Input for Extra Cheese")

print(f"Your Final bill is {bill}")
