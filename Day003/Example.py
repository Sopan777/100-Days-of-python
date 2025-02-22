print("Welcome to roller Coster:")

height = int(input("Enter your Height:"))
bill=0
if height >= 120:
    print("You can ride Roller Coster")
    age = int(input("Enter your age: "))

    if age < 12:
        bill += 5
        print(f"Pleasr Pay ${bill}.")
    elif age <= 18:
        bill += 7
        print(f"Plese Pay $${bill}.")
    elif age >= 45 and age <= 55:
        bill +=0
        print("Your Ride is Completely free")
    else:
        bill += 12
        print(f"Please play ${bill}.")
        
    photo = input("Do you want a photo taken? Y or N :")
    if photo == "Y":
        bill +=3
        print(f"Plese Pay ${bill}.")
    else:
        print(f"Plese Pay ${bill}.")

else:
    print("You can not ride Roller Coster") 