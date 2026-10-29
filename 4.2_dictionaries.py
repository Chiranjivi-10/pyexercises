"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:the description of one marketing campaign, written directly in the code as
a dictionary with six fields.
# 2. Process:the program reads two fields, changes the monthly budget, removes the
temporary note field, then loops over the dictionary. It also asks for a field
that does not exist, first in the unsafe way and then in a safe way.
# 3. Out:the campaign name and channel, the budget before and after the change,
every remaining field with its value, and a message for the missing field
# 4. My object, my five fields, and why those:


# Your code below
campaign = {
    "name": "Winter Sale 2026",
    "channel": "Google Ads",
    "monthly_budget": 4500,
    "target_audience": "Customers aged 25-45 in Île-de-France",
    "start_date": "2026-11-15",
    "internal_note": "Budget to be reviewed",
}
print("Campaign name:", campaign["name"])
print("Channel:", campaign["channel"])
print("Budget before (EUR):", campaign["monthly_budget"])
campaign["monthly_budget"] = 5000
print("Budget after (EUR):", campaign["monthly_budget"])
del campaign["internal_note"]
print("All fields:")
for field, value in campaign.items():
    print(" ", field, ":", value)
    rate = campaign.get("conversion_rate", "not available")
print("Conversion rate:", rate)