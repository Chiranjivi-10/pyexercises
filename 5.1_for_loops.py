"""Exercise 5.1 — Doing the same thing to every item

WHAT THE PROGRAM MUST DO
    Take the list you built in exercise 4.0 and, for every item, display a line that
    combines the item, its position, and something computed about it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What did you compute for each item, and what does the reader learn from that line?

WHAT THE AI CANNOT KNOW
    Your list from 4.0, and what is worth computing about its items. Length of the name,
    share of a total, position in a ranking, whether the item passes a threshold you set.
    Open your 4.0 file, copy the list across, and say in a comment what you decided.

CHECK IT YOURSELF
    Count the lines your program printed. There must be exactly as many as items in your
    list. If there is one more or one less, you have an off-by-one, and it is worth
    understanding now rather than in the exam.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:the list of 8 monthly marketing budgets (EUR) copied from exercise 4.0
# 2. Process:the program calculates the total of the list, then loops over every
budget with enumerate() to get its position (starting at 1) and calculates
its share of the total as a percentage.
# 3. Out:one line per budget showing its position, its amount and its share of
the total, then a final line with the number of lines printed.
# 4. What I compute for each item, and why it is worth showing:
The share of the total budget (budget / total * 100). The reader sees at a
glance which channels take most of the money. For example, position 1 (Google
Ads) takes about a quarter of the spend, while position 4 (Email) takes
only about 3%. An amount alone does not say that, a share does.


# Your code below
channels = ["Meta Ads", "Google Ads", "LinkedIn Ads", "TikTok Ads",
            "Email", "affiliate marketing", "influencer marketing",
            "video marketing"]

for position, item in enumerate(channels, start=1):
    print(f"{item} - Position: {position} - Length: {len(item)}")
