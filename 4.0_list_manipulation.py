"""Exercise 4.0 — Working with a list

WHAT THE PROGRAM MUST DO
    Build a list of at least eight items, then display: the whole list, one item of your
    choice, the list sorted, and something computed from it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your list about, and what did you compute from it? Why is that number
       interesting?

WHAT THE AI CANNOT KNOW
    The content of your list. It must come from your own field: marketing channels,
    campaign names, product references, cities you operate in, monthly budgets. Not
    fruit, not "item1, item2, item3".

    Keep this file. Exercise 5.1 and exercise 6.0 both reuse the list you build here.

CHECK IT YOURSELF
    If you computed an average, a total or a maximum, work it out by hand on three of
    your items first, then check your program agrees on those three.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: input was the list of the marketing channels
# 2. Process:the program displays this list of items, one item of choice.
# 3. Out:he program displays the complete list, one selected marketing channel the sorted list, and the total monthly marketing budget.
# 4. What my list is about, and what I computed from it: list is about marketing channels and their monthly budgets.


# Your code below

channels = ["Meta Ads", "Google Ads", "LinkedIn Ads", "TikTok Ads", "Email", "affiliate marketing", "influencer marketing", "video marketing"]
print("the whole list :", channels)
print("how many items :", len(channels))
print("first          :", channels[0])
print("second         :", channels[1])
print("last           :", channels[-1])
print("second to last :", channels[-2])
print("whole list")



