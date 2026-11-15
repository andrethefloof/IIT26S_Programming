def cipher(text):
    LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
    UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipheredt = ""
    for char in text:
        if char in LOWER_ALPHABETS:
            index = (LOWER_ALPHABETS.index(char) + 3) % 26
            cipheredt += LOWER_ALPHABETS[index]
        elif char in UPPER_ALPHABETS:
            index = (UPPER_ALPHABETS.index(char) + 3) % 26
            cipheredt += UPPER_ALPHABETS[index]
        else:
            cipheredt += char
    return cipheredt
def saveToFile(filename, text):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
def main():
    fullt = ""
    print("Program starting.\n")
    print("Collecting plain text rows for ciphering.")
    while True:
        line = input("Insert row(empty stops): ")
        if line == "":
            break
        if fullt == "":
            fullt = line
        else:
            fullt += "\n" + line
    print()
    print("#### Ciphered text ####")
    cipheredt = cipher(fullt)
    print(cipheredt)
    print()
    print("### Ciphered text ###")
    filename = input("Insert filename to save: ")
    saveToFile(filename, cipheredt)
    print("Ciphered text saved!")
    print("Program ending.")
main()