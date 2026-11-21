"""Exercise 9.0 — Surviving what you did not expect

Useful for the final exam: two campaigns in the exam dataset have zero conversions.

WHAT THE PROGRAM MUST DO
    Ask the user for a number, divide something by it, and keep running whatever the
    user types. Never crash.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two different failures can happen here, and should they produce the same
       message to the user? Decide before coding.

WHAT THE AI CANNOT KNOW
    Your answer to question 4, and how many attempts you allow before giving up.

    An assistant will often propose catching every error at once. Find out why catching
    each failure separately is better, and write the reason in a comment.

CHECK IT YOURSELF
    Run it with: a normal number, then zero, then the word "abc", then an empty line.
    Four runs, four behaviours, all described in a comment. If any of them stopped your
    program, it is not finished.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:The user enters a number.
# 2. Process:Divide 100 by the number using try and except.
# Allow the user to try again if an error occurs.

# 3. Out:Display the result or an error message.

# 4. The two failures, and whether they deserve the same message:ZeroDivisionError: The user enters 0.
# ValueError: The user enters text or an empty line.
# They need different messages because the errors are different.



# Your code below
for attempt in range(4):

    try:
        number = float(input("Enter a number: "))

        result = 100 / number

        print("Result:", result)
        break

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

    except ValueError:
        print("Error: Please enter a valid number.")

else:
    print("Too many attempts. Program ended.")

print("Thank you!")
