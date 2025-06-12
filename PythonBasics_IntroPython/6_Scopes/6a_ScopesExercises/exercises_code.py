# Python Basics Exercises: Functions and Loops
# https://realpython.com/courses/python-basics-exercises-scopes/

# Review Exercises: LEGB

# ----

# Ask for the Addresses

# def explore_basement():
#     def explore_cabinet():
#         address = "Cookie Cabinet"
#         print(address)
        
#     address = "Mouse House"
#     explore_cabinet()
#     print(address)

# address = "Python Palace"
# explore_basement()
# print(address)

# ----

# Adjust the Addresses
# Make "Cookie Cabinet" the global variable

# def explore_basement():
#     def explore_cabinet():
#         global address
#         address = "Cookie Cabinet"
#         print(address)
        
#     address = "Mouse House"
#     explore_cabinet()
#     print(address)

# address = "Python Palace"
# explore_basement()
# print(address)

# -------------------------------------------------

# Deliver the Invitation Exercise

# def visit_woods(my_invitation):
#     if "my_invitation" in locals():
#         print(my_invitation)
        
# invitation = "Let's have a party!"
# visit_woods(invitation)

# -------------------------------------------------

# Collect All Cookies Exercise

# def on_the_shelf():
#     shelf_cookies = ["Peanut", "Chocolate"]
#     return shelf_cookies
    
# def under_the_sofa():
#     sofa_cookies = ["Oat", "Salted Caramel"]
#     return sofa_cookies

# cookies = []
# cookies = on_the_shelf() + under_the_sofa()
# print(cookies)

# -------------------------------------------------

# Rename the Palace
# Adjust the code below so the last line of the program prints "Mouse House".

def explore_basement():
    def explore_cabinet():
        """🐭"""
        address = "Cookie Cabinet"
        print(address)
        
    address = "Mouse House"
    explore_cabinet()
    print(address)
    return address
    
address = "Python Palace"
print(explore_basement())