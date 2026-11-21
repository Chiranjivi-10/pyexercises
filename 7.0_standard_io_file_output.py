"""Exercise 7.0 — Collecting data and saving it

WHAT THE PROGRAM MUST DO
    Ask the user for the information needed to record one entry, then save it to a CSV
    file. Running the program twice must produce two entries, not overwrite the first.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?  (name your file, and list your columns)
    4. Which columns did you choose, and what would you actually do with this file once
       it has two hundred rows in it?

WHAT THE AI CANNOT KNOW
    Your columns. They must be the ones you would really need to collect for a purpose
    you can state. See 7.0_student_data.csv for the shape of a header line, not for
    the columns to use.

    Two behaviours are yours to decide, and an assistant will guess them wrong:
    what happens the very first time, when the file does not exist yet and needs its
    header line, and what happens when a value the user typed is not acceptable.

CHECK IT YOURSELF
    Run your program three times with different values. Then open the file and count
    the lines. You should have three entries and exactly one header line. If you have
    three header lines, or one entry, your program is wrong.

DELIVERABLE
    This file, plus the CSV your program produced.
"""

# 1. In:
# 2. Process:
# 3. Out, file name and columns:
# 4. Why these columns, and what this file is for:


# Your code below
import csv
import os

filename = "students.csv"

name = input("Enter student name: ")
age = input("Enter student age: ")
course = input("Enter course: ")

if name == "" or not age.isdigit() or course == "":
    print("Invalid input. Please try again.")

else:
    new_file = not os.path.exists(filename)

    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)

        if new_file or os.path.getsize(filename) == 0:
            writer.writerow(["Name", "Age", "Course"])

        writer.writerow([name, age, course])

    print("Student data saved successfully!")
