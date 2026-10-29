"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The user enters marketing channel names, such as Meta Ads, Google Ads, or Email. The user types "stop" to finish.
# 2. Process:Create an empty list to store the channels.



Use a while loop to keep asking for channel names.



If the user types "stop", end the loop.



Otherwise, add the channel to the list c the total number of channels entered.
# 3. Out:Display the total number of channels entered and the list of channel names
# 4. My stop condition, my attempt limit, my summary:
When the user types "stop", the loop ends.
There is no fixed attempt limit; the user can enter as many marketing channels as they want until they type "stop"
The program displays all the marketing channels entered and the total number of channels collected.


# Your code below
channels = []

while True:
    channel = input("Enter a marketing channel (or type 'stop' to finish): ")

    if channel.lower() == "stop":
        break

    channels.append(channel)
    print("Channel added:", channel)

print("\n--- Summary ---")
print("Total channels entered:", len(channels))
print("Channels entered:", channels)

