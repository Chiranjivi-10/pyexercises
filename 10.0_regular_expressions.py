"""Exercise 10.0 — Checking the shape of text (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Validate three pieces of information typed by the user, and only save them when all
    three are acceptable.

ANSWER THESE FIRST, in comments
    1. What goes in?:-Name, email, and phone number
    2. What happens to it?:-Check if all inputs are valid
    3. What comes out?:-Save valid data in details.txt
    4. What are your three fields, and what makes a value acceptable for each? Write the
       rule in plain English before writing any pattern.:-Name: Only letters, minimum 2 characters
# Email: Must contain @ and a domain
# Phone: Exactly 10 digits


WHAT THE AI CANNOT KNOW
    Your three rules. "A valid email" is not a rule, it is a wish. Say what you accept
    and what you reject, and be ready to defend a borderline case.

WHAT TO WATCH
    An assistant will hand you a pattern that looks like line noise. Do not accept it
    until it has explained it to you piece by piece, and you have written that
    explanation in your own words above it.

CHECK IT YOURSELF
    For each field, prepare one value that must pass and two that must fail. Run all
    nine. Any surprise goes in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# Your code below
import re

name = input("Enter name: ")
email = input("Enter email: ")
phone = input("Enter phone number: ")

# Check name, email, and phone
name_ok = re.fullmatch(r"[A-Za-z]{2,}", name)
email_ok = re.fullmatch(r"[A-Za-z0-9._]+@[A-Za-z0-9]+\.[A-Za-z]{2,}", email)
phone_ok = re.fullmatch(r"[0-9]{10}", phone)

if name_ok and email_ok and phone_ok:
    with open("details.txt", "a") as file:
        file.write(name + "," + email + "," + phone + "\n")

    print("Data saved successfully!")

else:
    print("Invalid input! Data not saved.")
