num1=float(input("Enter 1st Value: "))
op=input("Enter Operator:")
num2=float(input("Enter 2nd Value: "))

if op=="+":
    add=num1+num2
    print(add)
elif op=="-":
    sub=num1-num2
    print(sub)
elif op=="*":
    mult=num1*num2
    print(mult)
elif ZeroDivisionError:
    print("Cant divide by 0")
elif op=="/":
    div=num1/num2
    print(div)
else:
    print("Invalid, Try Again!")
