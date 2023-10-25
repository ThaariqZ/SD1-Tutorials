user_op=str(input("Do you like Python? \n"))
user_op=user_op.lower()
if user_op=="yes" and "y":
    print("You are on the right course")
elif user_op=="no" and "n":
    print("You might change your mind")
else:
    print("I did not understand")
