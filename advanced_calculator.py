#advanced calculator



from math import *
while True :
    ask = input("operate or find root or find logarithmic : " )

    if ask == "operate":

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operator = input("Enter operator: ")

        if operator == "+" :
            print(num1 + num2)
        elif operator == "-" :
            print(num1 - num2)
        elif operator == "*" :
            print(num1*num2)
        elif operator == "/":
            if num2 == 0:
                print("Undefined")
            else:
                print(num1/num2)
        elif operator == "%" :
            if num2 == 0:
                print("Undefined")
            else :
                print(num1%num2)
        elif operator == "^":
            if num2 == 0:
                print("1")
            else:
                print(num1**num2)

    elif ask == "find root" :
        num1 = float(input("enter a number"))
        if num1<=0 :
            print("Operation not supported")
        elif num1>0 :
            print(sqrt(num1))

    elif ask == "find logarithmic" :
        num1 = float(input("Enter a number: "))
        if num1<=0 :
            print("Operation not supported")
        else :
            print(log(num1, 10))

    else :
        print("Operation not supported")
    ans = input("Do you want to calculate again ? (y/n) ")
    if ans in'Nn':
        print('thanks for using this calculator')
        break










