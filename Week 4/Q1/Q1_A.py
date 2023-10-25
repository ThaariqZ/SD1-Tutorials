hidden = 6 

while True:
    try:
        guess = int(input("Enter a number between 1 and 20: "))

        if guess != hidden:
            print (guess, "is not correct")

        else:
            print (guess, "is correct")
            break
    except ValueError:
        print("Invalid input Try again")