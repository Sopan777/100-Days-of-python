print("Leap year calculator")

year = int(input("Enter year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 ==0:
            print(f"{year} is Leap year")
        else:
            print(f"{year} is Not a Leap year")
    else: 
        print(f"{year} is Leap year")
else:
    print(f"{year} is Not a Leap year")                