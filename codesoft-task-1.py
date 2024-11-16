while True:
    a=int(input("Enter the first operand:"))
    b=int(input("Enter the second operand:"))
    op=input("Enter the operator(+,-,*,/):")

    if op=='+':
        result=a+b
    elif op=='-':
        result=a-b
    elif op=='*':
        result=a*b
    elif op=='/':
        if b!=0:
            result=a/b
        else:
            print("ZeroDivisionError")
    else:
        print("Invalid operator")
    print("Result:",result)

    choice=input("Do you want to perform another operation(yes/no)?:")
    if choice.lower()=='yes':
        continue
    else:
        break