import sys
import random

ans = True

while ans:
    question = input("Ask the magic 8 ball a question: (press enter to quit)")

    answers = random.randint(1, 8)

    if question == "":
        sys.exit()
    elif answers == 1:
        print("It is certain")

    elif answers == 2:
        print("Outlook looks good")

    elif answers == 3:
        print("You can rely on that")

    elif answers == 4:
        print("Sorry, but no")

    elif answers == 5:
        print("Outcome looks exciting")

    elif answers == 6:
        print("Maybe")

    elif answers == 7:
        print("Have fun!")

    elif answers == 8:
        print("Sure")