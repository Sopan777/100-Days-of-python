import art

def addition(n1, n2):
    return n1 + n2

def substraction(n1, n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

def divison(n1, n2):
    return n1 / n2

operations = { 
    "+": addition,
    "-": substraction,
    "*": multiplication, 
    "/": divison
    }
def Calculator():

    print(art.logo)

    num1 = float(input("What's the first number: "))

    for operand in operations:
        print(operand)

    recall = True
    while recall:
        
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number: "))
        calculaltion_function = operations[operation_symbol]
        answer = calculaltion_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        permission = input(f"Type 'y' to continue calculation with {answer}, or type 'n' to start new calculation: ")

        if permission == "y":
            num1 = answer
        else:
            recall = False
            Calculator()

Calculator()