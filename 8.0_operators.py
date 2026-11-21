"""Exercise 8.0 — Operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Take two values of your choice and display, as a readable table, the result of every
    comparison between them and of the logical combinations of those results.

ANSWER THESE FIRST, in comments
    1. What goes in?:-Two numbers
    2. What happens to it?:-Compare the numbers using operators
    3. What comes out?:-Display comparison and logical results
    4. Which two values did you pick, and which comparison result surprised you?:-10 and 20

WHAT THE AI CANNOT KNOW
    Your two values. Pick a pair where the answer is not obvious: two strings with
    different capitalisation, a number and the same number written as text, or zero and
    an empty string.

CHECK IT YOURSELF
    Predict each result before running. Count how many you got right.

DELIVERABLE
    This file, with your comments and your code.
"""

# Your code below
a = 10
b = 20

print("Comparison Operators")
print("--------------------------")
print("a == b :", a == b)
print("a != b :", a != b)
print("a > b  :", a > b)
print("a < b  :", a < b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)

print("\nLogical Operators")
print("--------------------------")
print("AND :", (a < b) and (a != b))
print("OR  :", (a > b) or (a < b))
print("NOT :", not (a == b))
