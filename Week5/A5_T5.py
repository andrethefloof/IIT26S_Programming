def insert_word():
    word = input("Insert word: ")
    return word
def show_word(word):
    print(f'Current word - "{word}"')
def show_word_reverse(word):
    print(f'Word reversed - "{word[::-1]}"')
def main():
    print("Program starting.")
    word = None
    while True:
        print("Options:")
        print("1 - Insert word")
        print("2 - Show current word")
        print("3 - Show current word in reverse")
        print("0 - Exit")
        input_choice = input("Your choice: ")
        if input_choice == "1":
            word = insert_word()
        elif input_choice == "2":
            show_word(word)
        elif input_choice == "3":
            show_word_reverse(word)
        elif input_choice == "0":
            print("Exiting program.\n")
            print("Program ending.")
            break
        else:
            print("Unknown option! try again.")
main()