# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

Lower_case_name1 = name1.lower()
Lower_case_name1 = name2.lower()

T = int(name1.count('t')) + int(name2.count('t'))
R = int(name1.count('r')) + int(name2.count('r'))
U = int(name1.count('u')) + int(name2.count('u'))
E = int(name1.count('e')) + int(name2.count('e'))

True_Total = T + R + U + E
L = name1.count('l') + name2.count('l')
O = name1.count('o') + name2.count('o')
V = name1.count('v') + name2.count('v')
E = name1.count('e') + name2.count('e')

Love_Total = L + O + V + E

Love_Score = int(str(True_Total) + str(Love_Total))

if Love_Score < 10 or Love_Score > 90:
    print(f"Your score is {Love_Score}, you go together like coke and mentos.")
elif Love_Score > 40 and Love_Score < 50:
    print(f"Your score is {Love_Score}, you are alright together.")
else: 
    print(f"Your score is {Love_Score}.")

