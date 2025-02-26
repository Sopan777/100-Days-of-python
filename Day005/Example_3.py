for num in range (1, 101):
    
    if num % 3 == 0 and num % 5 == 0 :
        num = "FizzBuzz"
        print(num)
    elif num % 5 == 0 :
        num = "Buzz"
        print(num)
    elif num % 3 == 0 : 
        num = "Fizz"
        print(num)
    else:
        print(num)