from calc_art import logo
import os
print(logo)
def operation(a,o,b):
    if o=="+":
        return a+b
    elif o=="-":
        return a-b
    elif o=="*":
        return a*b
    elif o=="/":
        return a/b
choice='n'
while choice=='n':
    a=float(input("What's the first number?: "))
    print(" + \n - \n * \n / ")
    choice='y'
    while choice=='y':
        o=input("Pick an operation: ")
        b=float(input("What's the next number?: "))
        output=operation(a,o,b)
        print(f"{a} {o} {b} = {output}")
        choice=input(f"Type 'y' to continue calculating with {output}, or type 'n' to start a new calculation, or type '#' to exit: ")
        if choice=='y':
            a=output
        elif choice=='n':
            os.system('cls')
        else:
            break