"""Exercise 2.1 — Transforming text (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it with a sentence that has spaces at both ends and a capital in the middle.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:the program takes one sentence entered by the user.
# 2. Process:the program applies four different string transformationsto the sentence.
# 3. Out:the program displays different version of the same sentence.
# 4. My four transformations, and when each is useful:1. upper() - Useful for displaying text in capital letters.
2. lower() - Useful for converting text to lowercase.
3. title() - Useful for capitalizing the first letter of each word.
4. strip() - Useful for removing spaces at the beginning and end.



# Your code below
sentence=input("type a sentence:")
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("Title case:", sentence.title())
print("Without extra spaces:", sentence.strip())