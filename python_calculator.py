def add(a,b) :
    return a+b
def substract(a,b) :
    return a-b
def multiply(a,b) :
    return a*b
def divide(a,b) : 
    if b != 0 :
        return a/b
    else :
        return "cannot devide by 0 "
while True :
    print("this is a simple calculator ")
    
    try :
        num1 = float(input("enter first number : "))
        num2 = float(input("enter second number : "))
    except :
        print("invalid input , please enter only numbers")
    operation = input("chose operation ('*' '/' '+' '-') or 'done' to exit  : ")
    if operation == "done" :
        print ("good bye !")
    if operation == "+" :
        result = add(num1,num2)
    elif operation == "-" :
        result =substract(num1,num2)
    elif operation == "*" :
        result=multiply(num1,num2)
    elif operation == "/" :
        result =divide(num1,num2)
    print ("Result : " ,result )
