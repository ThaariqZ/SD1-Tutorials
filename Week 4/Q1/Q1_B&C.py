import random 
hidden = random.randint(1,20) 

while True:

    guess = int(input("Enter Your Guess"))

    if guess != hidden:
        print (guess, "is not correct")

        if guess>hidden:
            print("The value is higher than the hidden value\n")

        else:
            print("The value is lower than the hidden value\n")

    else:
        print (guess, "is correct")
        break
