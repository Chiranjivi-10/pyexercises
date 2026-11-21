
# Name: Chiranjivi Badwe
# Group: CL05
#
# 1. Input: scenarios_A.csv with comma-separated values.
#    It contains scenarios, options, budget changes,
#    reputation changes and feedback.
#
# 2. Process: Read scenarios, shuffle them, ask the
#    player to choose A, B or C, and update both gauges.
#
# 3. Output: Final result, best and worst moves,
#    and results.csv containing name, budget,
#    reputation, title and date.
#
# 4. Possible problems:
#    Invalid choice: ask again.
#    Missing file: display an error.
#    Budget or reputation at zero: end the game.
#
# Extra feature: Difficulty
# Easy starts at 15000 EUR and hard at 6000 EUR.

import csv
import random
from datetime import date
from pathlib import Path

FOLDER = Path(__file__).resolve().parent


# Function 1: Read scenarios from the CSV file
def load_scenarios():
    scenarios = []

    with open(FOLDER / "scenarios_A.csv",
              newline="", encoding="utf-8-sig") as file:

        reader = csv.DictReader(file)

        for row in reader:
            options = {}

            for letter in "ABC":
                options[letter] = (
                    row["Option" + letter],
                    int(row["Budget" + letter]),
                    int(row["Reputation" + letter]),
                    row["Feedback" + letter]
                )

            scenarios.append((row["Scenario"], options))

    return scenarios


# Function 2: Ask the player to choose A, B or C
def ask_choice():
    while True:
        choice = input("Your choice (A, B or C): ")
        choice = choice.strip().upper()

        if choice in ("A", "B", "C"):
            return choice

        print("Please type A, B or C.")


# Function 3: Choose difficulty
def ask_difficulty():
    while True:
        difficulty = input(
            "Difficulty (easy/hard): "
        ).strip().lower()

        if difficulty == "easy":
            return 15000

        elif difficulty == "hard":
            return 6000

        print("Please type easy or hard.")


# Function 4: Update budget and reputation
def apply_choice(budget, reputation, option):
    text, budget_change, reputation_change, feedback = option

    budget = budget + budget_change
    reputation = reputation + reputation_change

    reputation = min(100, reputation)

    return budget, reputation


# Function 5: Calculate final title
def get_title(score):
    if score < 95:
        return "Eternal Intern"

    elif score < 120:
        return "Growth Hacker"

    elif score < 140:
        return "CMO Material"

    else:
        return "Viral Legend"


# Function 6: Save game results
def save_result(name, budget, reputation, title):
    filename = FOLDER / "results.csv"

    new_file = (
        not filename.exists()
        or filename.stat().st_size == 0
    )

    with open(filename, "a", newline="",
              encoding="utf-8") as file:

        writer = csv.writer(file)

        if new_file:
            writer.writerow([
                "name", "budget", "reputation",
                "title", "date"
            ])

        writer.writerow([
            name,
            budget,
            reputation,
            title,
            date.today().isoformat()
        ])


# Function 7: Run the complete game
def play_game():

    print("WELCOME TO SURVIVE THE QUARTER!")

    name = input("What is your name? ").strip()

    if name == "":
        name = "Player"

    budget = ask_difficulty()
    reputation = 50

    try:
        scenarios = load_scenarios()

    except (FileNotFoundError, KeyError,
            ValueError, csv.Error) as error:
        print("Could not load scenarios_A.csv:", error)
        return

    if len(scenarios) < 10:
        print("At least 10 scenarios are required.")
        return

    random.shuffle(scenarios)

    history = []
    fired_reason = ""

    # Play 10 days
    for day, (situation, options) in enumerate(
        scenarios[:10], start=1
    ):

        print("\n--- Day", day, "---")
        print("Budget:", budget, "EUR")
        print("Reputation:", reputation, "/100")

        print("\nSituation:")
        print(situation)

        print("\nOptions:")

        for letter in "ABC":
            print(letter + ":", options[letter][0])

        choice = ask_choice()

        option = options[choice]

        text, budget_change, reputation_change, feedback = option

        budget, reputation = apply_choice(
            budget, reputation, option
        )

        history.append((
            reputation_change,
            day,
            text
        ))

        print("\nResult:")
        print(feedback)

        print("Budget change:", budget_change)
        print("Reputation change:", reputation_change)

        print("New budget:", budget)
        print("New reputation:", reputation)

        # Stop if the player is fired
        if budget <= 0:
            fired_reason = "Budget reached zero or below."
            break

        if reputation <= 0:
            fired_reason = "Reputation reached zero or below."
            break

    # Display final result
    print("\n==============================")

    if fired_reason:
        title = "Fired"
        print("GAME OVER! You are fired.")
        print("Reason:", fired_reason)

    else:
        score = reputation + budget // 200
        title = get_title(score)

        print("Quarter survived!")
        print("Final score:", score)
        print(name + ", your title:", title)

    print("Budget left:", budget, "EUR")
    print("Reputation:", reputation, "/100")

    # Find best and worst decisions
    if history:
        best = max(history, key=lambda move: move[0])
        worst = min(history, key=lambda move: move[0])

        print(
            "Best move: Day", best[1],
            "-", best[2],
            "(" + str(best[0]) + ")"
        )

        print(
            "Worst move: Day", worst[1],
            "-", worst[2],
            "(" + str(worst[0]) + ")"
        )

    # Save results
    try:
        save_result(name, budget, reputation, title)
        print("\nSaved in results.csv")

    except OSError as error:
        print("Could not save results:", error)


# Start the game
if __name__ == "__main__":
    play_game()
