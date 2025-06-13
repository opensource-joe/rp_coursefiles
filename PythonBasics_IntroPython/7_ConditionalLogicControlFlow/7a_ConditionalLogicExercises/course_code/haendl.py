# Ask the user to enter an integer.
# Repeat the process if the user hasn't entered an integer.
while True:
    try:
        users_integer = int(input("Enter an integer: "))
        print(users_integer)
        break
    except ValueError:
        print("Please try again!")
