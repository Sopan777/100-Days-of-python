height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

BMI = float(weight) / (float(height) * float(height))
# BMI = float(weight) / float(height) ** 2 
print(BMI) 