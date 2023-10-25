hidden = 6 


def get_user_number():
    user_number:  int | None = None

    while user_number is None:
        try:
            user_input = int(input("ENter a number between 1 and 20: "))

        except ValueError:
            print("Use a number between 1 and 20: ")
            return get_user_number()
        
    return user_number
6
user_input = get_user_number()

while user_input != hidden:
    print(f"{user_input} is not the hidden number")
    user_input=get_user_number()