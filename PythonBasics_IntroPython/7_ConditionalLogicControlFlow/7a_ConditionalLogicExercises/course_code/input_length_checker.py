# Display whether the length of a user input
# is <, >, == 5 characters

string_to_check = input("Check string length: ")
string_length = len(string_to_check)

if string_length < 5:
    print("Your input is less than 5 characters long.")
elif string_length > 5:
    print("Your input is greater than 5 characters long.")
else:  # == 5
    print("Your input is 5 characters long.")
