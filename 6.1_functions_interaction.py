"""Exercise 6.1 — Small functions working together

WHAT THE PROGRAM MUST DO
    Write three small functions, each doing one thing, and a fourth that uses the other
    three to answer one question about your data.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?  (say which function does what, in order)
    3. What comes out?
    4. What question does your fourth function answer, and why does splitting it into
       three make it easier to check?

WHAT THE AI CANNOT KNOW
    Your question and your split. Ask an assistant for "three functions" and it will
    invent three; they will not be the three your question needs. Decide the split first,
    on paper, then ask.

    One function, one job. If you cannot describe what one of yours does in a single
    sentence without using the word "and", it is doing two things.

CHECK IT YOURSELF
    Test each of the three small functions on its own before combining them. Write in a
    comment the input and expected output you used for each. That is three test cases,
    and they are part of the deliverable.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A list of numbers
# 2. Process, function by function:find sum, count, and average
# 3. Out:average of numbers
# 4. The question my fourth function answers:what is the average


# Your code below
def total(numbers):
    return sum(numbers)

def count(numbers):
    return len(numbers)

def average(sum_value, count_value):
    if count_value == 0:
        return 0
    return sum_value / count_value

def calculate_average(numbers):
    a = total(numbers)
    b = count(numbers)
    c = average(a, b)
    return c
print(total([10, 20, 30]))
print(count([10, 20, 30]))
print(average(60, 3))
print(calculate_average([10, 20, 30]))