import time
import random
import select
import sys


money = 100
numbers = random.randint(1, 20)
objects = random.choice(["bananas", "nails", "watches", "diamonds", "gold coins"])
operation = random.choice(["+", "-", "*", "/", "//", "**"])


def display(text, speed=0.03):
    for letter in text:
        print(letter, end="", flush=True)
        time.sleep(speed)


def Brain():

    global money

    display("\nMOC: Very well. Let's begin.\n")
    display(f"You currently have {money} gold coins.\n")
    display("Each correct answer earns you 20 coins.\n")
    display("Each incorrect answer costs you 10 coins.\n")

    rounds = 5

    for round_number in range(1, rounds + 1):

        print("\n" + "=" * 40)
        print(f"              ROUND {round_number}/{rounds}")
        print("=" * 40)

        # Generate the riddle

        operation = random.choice(["+", "-", "*", "/", "//", "**"])
        objects = random.choice(["bananas", "nails", "watches", "diamonds", "gold coins"])

        a = random.randint(2, 10)
        b = random.randint(2, 10)

        if operation == "+":

            result = a + b
            question = f"You have {a} {objects}. I give you {b} more. How many do you have?"

        elif operation == "-":

            if b > a:
                a, b = b, a

            result = a - b
            question = f"You have {a} {objects}. You spend {b} of them. How many do you have left?"

        elif operation == "*":

            result = a * b
            question = f"You have {a} chests, each containing {b} {objects}. How many do you have in total?"

        elif operation == "/":

            result = a
            a = a * b
            question = f"You have {a} {objects}. You distribute them equally among {b} people. How many does each person receive?"

        elif operation == "//":

            result = a // b
            a = a * b + random.randint(0, b - 1)
            result = a // b
            question = f"You have {a} {objects}. You divide them into groups of {b}. How many complete groups can you make?"

        elif operation == "**":

            a = random.randint(2, 4)
            result = a ** 2
            question = f"You have {a} chests, each containing {a} bags of {objects}. How many bags do you have in total?"

        # Display the riddle

        print("\nMOC:")
        display(question + "\n")

        print("\nYou have 15 seconds to answer.")

        start_time = time.time()

        # Receive the answer with a time limit

        print("\nYour answer: ", end="", flush=True)

        ready, _, _ = select.select([sys.stdin], [], [], 15)

        if ready:
            answer = sys.stdin.readline().strip()

            try:
                answer = int(answer)

                duration = time.time() - start_time

                if answer == result:

                    display("\nMOC: Correct answer.\n")
                    money += 20
                    display("+20 gold coins.\n")

                else:

                    display(f"\nMOC: Wrong answer. The correct answer was {result}.\n")
                    money -= 10
                    display("-10 gold coins.\n")

            except ValueError:

                display("\nMOC: I asked for a number, not something else.\n")
                money -= 10

        else:

            display("\n\nMOC: Time is up.\n")
            display(f"The correct answer was {result}.\n")
            money -= 10

        print(f"\nCurrent balance: {money} gold coins.")

        # Check for bankruptcy

        if money <= 0:

            display("\nMOC: You are bankrupt. The game is over.\n")
            break

        time.sleep(1)

    # End of the game

    print("\n" + "=" * 40)
    print("              GAME OVER")
    print("=" * 40)

    if money > 100:

        display(f"\nMOC: You leave with {money} gold coins.\n")
        display("You managed to make a profit. Congratulations.\n")

    elif money == 100:

        display("\nMOC: You leave with your initial capital.\n")
        display("Neither a winner nor a loser.\n")

    else:

        display(f"\nMOC: You leave with {money} gold coins.\n")
        display("You lost money. You will have to do better next time.\n")


# INTRODUCTION

intro = """
I am MOC, the banker.

I propose a game. I will present you with several mathematical riddles
and you will have to answer within the time limit.

Each correct answer will earn you money.
However, every mistake will cost you part of your capital.

Think carefully before answering.
"""

display(intro)

ask = input("\nAre you in? Answer Yes or No: ")

if ask.lower().strip() in ["yes", "y"]:

    Brain()

else:

    display("\nMOC: Perhaps another time.\n")