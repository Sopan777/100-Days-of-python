#Write your code below this line 👇
def prime_checker(number):
    Is_prime = True
    for num in range(2, number):
        if number % num == 0 :
            Is_prime = False
    if Is_prime:
        print("It's a prime number.")
    if not Is_prime:
        print("It's not a prime number.")


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



