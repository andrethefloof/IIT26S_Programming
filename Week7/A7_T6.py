import random
random.seed(1234)

CHOICES = {
    1: "rock",
    2: "paper",
    3: "scissors",
}
HANDS = {
    "rock": """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    "paper": """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
    "scissors": """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""",
}
def main():
    owins = 0
    olosses = 0
    pwins = 0
    plosses = 0
    draws = 0
    print("Program starting.")
    print("Welcome to the rock-paper-scissors game!")
    name = input("Insert player name: ")
    print(f"Welcome {name}!")
    print("Your opponent is RPS-3PO.")
    print("Game starts...")
    while True:
        print()
        menuoptions()
        choice = choiceoptions()
        if choice == 0:
            finalresults(name, owins, olosses, pwins, plosses, draws)
            break
        opponent_choice = botchoice()
        pmove = playerchoice(choice)
        omove = playerchoice(opponent_choice)
        print()
        print("#########################")
        print(f"{name} chose {pmove}.")
        print()
        print(HANDS[pmove])
        print()
        print("#########################")
        print(f"RPS-3PO chose {omove}.")
        print()
        print(HANDS[omove])
        print()
        print("#########################")
        print()
        owins, olosses, pwins, plosses, draws = displayresults(
            name, pmove, omove, owins, olosses, pwins, plosses, draws
        )
def menuoptions():
    print("Options:")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")
    print("0 - Quit game")
def choiceoptions():
    choice = int(input("Your choice: "))
    while True:
        if choice == 1:
            print("Rock! Paper! Scissors! Shoot!")
            return choice
        elif choice == 2:
            print("Rock! Paper! Scissors! Shoot!")
            return choice
        elif choice == 3:
            print("Rock! Paper! Scissors! Shoot!")
            return choice
        elif choice == 0:
            return choice
        else:
            print("Invalid choice. Please try again.")
def playerchoice(choice: int):
    return CHOICES[choice]
def botchoice():
    return random.randint(1, 3)
def displayresults(
    name: str,
    pmove: str,
    omove: str,
    owins: int,
    olosses: int,
    pwins: int,
    plosses: int,
    draws: int,
):
    if pmove == omove:
        print(f"Draw! Both players chose {pmove}.")
        draws += 1
    elif (
        (pmove == "rock" and omove == "scissors")
        or (pmove == "paper" and omove == "rock")
        or (pmove == "scissors" and omove == "paper")
    ):
        print(f"{name} {pmove} beats RPS-3PO {omove}.")
        pwins += 1
        olosses += 1
    else:
        print(f"RPS-3PO {omove} beats {name} {pmove}.")
        owins += 1
        plosses += 1
    return owins, olosses, pwins, plosses, draws
def finalresults(name: str, owins: int, olosses: int, pwins: int, plosses: int, draws: int):
    print()
    print("Results:")   
    print(f"{name} - wins ({pwins}), losses ({plosses}), draws ({draws})")
    print(f"RPS-3PO - wins ({owins}), losses ({olosses}), draws ({draws})")
    print()
    print("Program ending.")
if __name__ == "__main__":
    main()