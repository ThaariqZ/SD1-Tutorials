num=int(input("if C->F (1)  or if F-> C (2): "))

if num==1:
    cel=int(input("Enter Celcius value: "))
    f=(cel*1.8)+32
    print("Farenheit= ",f)

elif num==2:
    far=int(input("Enter Farenheit value: "))
    c=(far-32)/1.8
    print("Celcius= ",c)

else:
    print("Invalid operation entered")
