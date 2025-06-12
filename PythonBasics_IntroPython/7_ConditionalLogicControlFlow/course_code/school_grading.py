"""
A: 70+
B: 60-69
C: 50-59
F: less than 50
"""

grade = 49

if grade >= 70:
    print("You passed with an 'A'")
elif grade >= 60:
    print("You passed with an 'B'")
elif grade >= 50:
    print("You passed with an 'C'")
else:
    print("You failed :(")

print("Grading done.")
