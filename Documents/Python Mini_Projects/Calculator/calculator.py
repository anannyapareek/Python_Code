def add(n1, n2):
    return n1 + n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

operations={ "+": add,
            "-":sub,
            "*":mul,
            "/":div }


def calculator():
    num1 = float(input("Enter value 1: "))
    cont = True

    while cont:
        op = input("Enter a mathematical operator(+,-,*,/): ")
        num2 = float(input("Enter value 2: "))
        output=operations[op](num1,num2)
        print(f"The output is {output}")
        choice = input(f"Type 'y' to continue calculating with {output}, or type 'n' to start a new calculation: ")
        if choice=="y":
            num1=output
        else:
            cont = False
            print("\n" * 20)
            calculator()


calculator()