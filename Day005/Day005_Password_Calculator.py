#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Generating Random items from the 
password = []
for passw in range (1, nr_letters + 1):
    random_letter = random.choice(letters)
    password.append(random_letter)

for passw in range (1, nr_symbols + 1):
    random_symbol = random.choice(symbols)
    password.append(random_symbol)

for passw in range (1, nr_numbers + 1):
    random_number = random.choice(numbers)
    password.append(random_number)

# Shuffling the result and printing it

random.shuffle(password)

final_password = ""
for passw in range (0, len(password)): 
    final_password += password[passw]
print(final_password)

    

