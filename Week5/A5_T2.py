def frameword(Pword):
    print(f'*' * (len(Pword)+4))
    print(f"* {Pword} *")
    print(f'*' * (len(Pword)+4))
    return None
def main():
    print("Program starting.")
    word = input("Insert a word: ")
    frameword(word)
    print("Program ending.")
    return None
main()