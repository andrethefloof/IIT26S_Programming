def main():
    print("Program starting.")
    count = 0
    while True:
        showOptions()
        input_choice = askChoice()
        if input_choice == "1":
            print(f"Current count - {count}")
        elif input_choice == "2":
            count += 1
            print(f"Count increased!")
        elif input_choice == "3":
            count = 0
            print("Cleared count!")
        elif input_choice == "0":
            print("Exiting program.\n")
            print("Program ending.")
            break
def showOptions():
    print("Options:")
    print("1 - Show count")
    print("2 - Increase count")
    print("3 - Reset count")
    print("0 - Exit")
    return None
def askChoice():
    choice = input("Your choice: ")
    if choice.isnumeric():
        return choice
    else:
        print("Unknown option!\n")
main()