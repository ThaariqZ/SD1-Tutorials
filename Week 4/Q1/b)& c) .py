import random 
hidden = 6 

while True:

    guess = random.randint(1,20)

    if guess != hidden:
        print (guess, "is not correct")

        if guess>hidden:
            print("The value is higher than the hidden value\n")

        else:
            print("The value is lower than the hidden value\n")

    else:
        print (guess, "is correct")
        break
