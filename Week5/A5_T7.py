DELIMITER = ","
def main():
    print("Program starting.")
    words = collectWords()
    analyseWords(words)
def collectWords():
    words = ""
    while True:
        word = input("Insert word(empty stops): ")
        if word == "":
            break
        if words:
            words += DELIMITER
        words += word
    return words
def analyseWords(words):
    word_list = words.split(DELIMITER) if words else []
    Avg = sum(len(word) for word in word_list) / len(word_list) if word_list else 0
    print(f"- {len(word_list)} Words")
    print(f"- {sum(len(word) for word in word_list)} Characters")
    print("- {:.2f} Average word length".format(Avg))
    print ("Program ending.")
main()