# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

BMI = round(weight/height**2)

if BMI < 18.5:
    print(f"Your BMI is {BMI}, You are Underweight")

elif (BMI < 25):
        print(f"Your BMI is {BMI}, You have a normal weight")

elif BMI > 25 and BMI < 30:
    print(f"Your BMI is {BMI}, You are overweight ")

elif BMI > 30 and BMI < 35:
    print(f"Your BMI is {BMI}, You are Obese")

elif BMI > 35:
    print(f"Your BMI is {BMI}, You are Clinically Obese")