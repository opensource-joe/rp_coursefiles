# Python Basics Exercises: Conditional Logic and Control Flow
# https://realpython.com/courses/conditional-logic-control-flow-exercises/

# Review Control Flow Strategies

# Control the Flow of Your Program
# Write a program that prompts the user to enter a word using the input() function and compares the length of the word to the number five. The program should display one of the following outputs, depending on the length of the user's input.

# "Your input is less than 5 characters long."
# "Your input is greater than 5 characters long."
# "Your input is 5 characters long."

# word = len(input("Enter a word "))

# if word < 5:
#     print("Your input is less than 5 characters long.")
# elif word > 5:
#     print("Your input is greater than 5 characters long.")
# else:
#     print("Your input is 5 characters long")

# ----

# Break Out of the Pattern - Exercise 1
# Using a break, write a program that repeatedly asks the user for some input and quits only if the user enters "q" or "Q".

# while True:
#     user_input = input("Enter something (or 'q' to quit): ")
#     if user_input.lower() == 'q':
#         break

# ----

# Break Out of the Pattern - Exercise 2
# Using continue, write a program that loops over the numbers 1 to 50 and prints all numbers that are not multiples of 3.

# for n in range(1, 51):
#     if n % 3 == 0:
#         continue
#     print(n)

# -----------------------------------------------------------------------

# Review Error Recovery and Event Simulation

# Recover From Errors
# Write a program that repeatedly asks the user to input an integer. If the user enters something other than an integer, then the program should catch the ValueError and display the message "Try again". Once the user enters an integer, the program should display the number back to the user and end without crashing.

# while True:
#     try:
#         user_input = int(input("Enter an integer: "))
#         break
#     except ValueError:
#         (print("That was not an integer"))

# ----

# Simulate Events
# Write a function called roll() that uses randint() to simulate rolling a fair die by returning a random integer between 1 and 6.

# import random

# def roll():
#     return random.randint(1, 6)

# print(roll())

# -----------------------------------------------------------------------

# Challenge

# Find the Factors of a Number
# A factor of a positive integer n is any positive integer less than or equal to n that divides n with no remainder.
# Write a program that asks the user to input a positive integer and then prints out the factors of that number. 

# user_input = int(input("Input a positive number. "))

# for divisor in range(1, user_input + 1):
#     if user_input % divisor == 0:
#         print(f"{divisor} is a factor of the {user_input}.")

# -----------------------------------------------------------------------

# Challenge: Build a Text-Based RPG

# Write a text-based role-playing game (RPG) with the following features:
# The game involves one player and one monster.

# The player begins with 100 health, while the monster starts with 150 health.

# The player has the options to attack, heal, or run away.

# If the player attacks, they deal between 10 and 15 damage to the monster.

# If the player heals, they regain 30 health, but can't exceed a maximum of 100.

# If the player runs away, the game concludes.

# After the player's turn, if the monster is still alive, it deals between 15 and 20 damage to the player.

# The game continues until the health of either the player or the monster reaches 0, or until the player decides to run away.

# import random

# print("Welcome to the role-playing game!")

# player_health = 100
# monster_health = 150
# heal = 30

# def is_factor_of_three(number):
#     if number % 3 == 0:
#         return True
#     else:
#         return False

# def calculate_damage_dealt_by(attacker):
#     if attacker == "player":
#         damage = random.randint(10, 15)
#     else:
#         damage = damage = random.randint(15, 20)
    
#     if is_factor_of_three(damage):
#         damage = damage * 2
#         print(f"{attacker.capitalize()} scored a critical hit of {damage} damage.a")
#     return damage

# while True:
    
#     print(f"Your health: {player_health}, Monster health: {monster_health}")
    
#     try:
#         action = input("Do you want to (A)ttack, (H)eal, or (R)un away: ").upper()
#     except KeyboardInterrupt:
#         print("You can't quit the game by pressing Ctrl_C.")
#         print("If you really want to leave, you'll need to (R)un away.")
    
#     # Here starts the players turn
#     if action == "A":
#         damage = calculate_damage_dealt_by("player")
#         monster_health -= damage
#         print(f"You attacked the monster for {damage} damage.")
        
#         if monster_health <= 0:
#             print("You defeated the monster.")
#             break
    
#     elif action == "H":
#         player_health += heal
#         if player_health > 100:
#             player_health = 100
#         print(f"You healed for {heal} health.")
    
#     elif action == "R":
#         print("You ran away!")
#         break
    
#     else:
#         print("Invalid action. Please choose A, H, or R.")
#         continue
    
#     # Here starts the monsters turn
#     if monster_health > 0:
#         monster_damage = calculate_damage_dealt_by("monster")
#         player_health -= monster_damage
#         print(f"The monster attacked you for {monster_damage} damage.")
        
#         if player_health <= 0:
#             print("You were defeated by the monster")
#             break