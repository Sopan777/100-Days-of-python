# Create a Tip calculator
# If the bill was $150.00, Split between 5 peoples, with 12% tip.
# Each person should pay (150.00\5)* 1.12 = 33.6

print("Welcome to to Tip Calculator")
bill = float(input("What was the total bil? "))
tip = int(input("What persent tip you would like to give? 10, 12 or 15? "))
people = int(input("How may people to split the bill? "))

pay = (bill / people) * (1+ (tip/100))
final_amount = "{:.2f}".format(pay)

print(f"Each person should pay: {final_amount}")

