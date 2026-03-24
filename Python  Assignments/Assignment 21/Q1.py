from Exception_handle import *
try:
    num1 = int(input("Enter the first number : "))
    num2 = int(input("Enter the second number : "))
except:
    print("Invalid input")
    
else:
    op = input("Enter operator : ")

    if op not in ['+','-','*','/']:
        raise OperatorException(op)

    if(op == '+'):
        print(num1 + num2)
    elif(op == '-'):
        print(num1 - num2) 
    elif(op == '*'):
        print(num1 * num2)
    elif(op == '/'):
        if(num2 == 0):
            raise ZeroDivideException(num2)      
        print(num1 / num2)

        
