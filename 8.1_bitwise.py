"""Exercise 8.1 — Bitwise operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Represent a set of permissions as bits, combine two of them, test whether a third is
    present, then add it and remove one.

ANSWER THESE FIRST, in comments
    1. What goes in?:-Marketing campaign permissions
    2. What happens to it?:-Combine, check, add, and remove permissions
    3. What comes out?:-Display permissions in binary
    4. What are your permissions about? Not files: invent a set from your own field,
       such as who may view, edit and publish a campaign.:-view, Edit, and Publish a campaign

WHAT THE AI CANNOT KNOW
    Your permission set and what each one means in your context.

CHECK IT YOURSELF
    Display the value in binary at each step and read the bits yourself.

DELIVERABLE
    This file, with your comments and your code.
"""

# Your code below
VIEW = 1       # 001
EDIT = 2       # 010
PUBLISH = 4    # 100

# Combine two permissions
permissions = VIEW | EDIT
print("Combined:", bin(permissions))

# Check if Publish permission exists
print("Can publish:", bool(permissions & PUBLISH))

# Add Publish permission
permissions = permissions | PUBLISH
print("After adding Publish:", bin(permissions))

# Remove Edit permission
permissions = permissions & ~EDIT
print("After removing Edit:", bin(permissions))
