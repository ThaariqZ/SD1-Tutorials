cost=float(input("Enter the Cost of the bill: "))
rate=int(input("Enter Rating"))
if rate==1:
    tip=cost*(20/100)
    print("Totaly Satisfied!")
    print("Tip amount is: ",tip)
elif rate==2:
    tip=cost*(15/100)
    print("Satisfied!")
    print("Tip amount is: ",tip)
elif rate==3:
    tip=cost*(10/100)
    print("Dissatisfied!")
    print("Tip amount is: ",tip)
else:
    print("Invalid Input")
