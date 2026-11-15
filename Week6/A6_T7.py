def cipher(text):
    LOWER_ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    UPPER_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ciphered_text = ""
    for char in text:
        if char in LOWER_ALPHABET:
            index = (LOWER_ALPHABET.index(char) + 13) % 26
            ciphered_text += LOWER_ALPHABET[index]
        elif char in UPPER_ALPHABET:
            index = (UPPER_ALPHABET.index(char) + 13) % 26
            ciphered_text += UPPER_ALPHABET[index]
        else:
            ciphered_text += char
    return ciphered_text
def readFile(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()
def writeFile(filename, text):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
def main():
    with open("player_progress.txt", "r", encoding="utf-8") as file:
        lines = file.read().splitlines()
    last_line = lines[-1]
    parts = last_line.split(";")
    currentLocation = int(parts[0])
    nextLocation = int(parts[1])
    cipheredPass = parts[2]
    locations = {
        0: "home",
        1: "Galba's palace",
        2: "Otho's palace",
        3: "Vitellius' palace",
        4: "Vespasian's palace"
    }
    currentLocation = locations[currentLocation]
    nextLocation = locations[nextLocation]
    passPhrase = cipher(cipheredPass)
    print("Travel starting.")
    print("Currently at " + currentLocation + ".")
    print("Travelling to " + nextLocation + "...")
    print("...Arriving to the " + nextLocation + ".")
    print("Passing the guard at the entrance.")
    print('"' + passPhrase + '"')
    print("Looking for the message in the palace...")
    messageFilename = str(nextLocation) + "_" + cipheredPass + ".gkg"
    cipheredMessage = readFile(messageFilename)
    messageLines = cipheredMessage.splitlines()
    print("Ah, there it is! Seems cryptic.")
    subId = nextLocation
    subNextId = nextLocation + 1 if nextLocation < 4 else 0
    newPass = messageLines[0] if messageLines else ""
    with open("player_progress.txt", "a", encoding="utf-8") as file:
        file.write(str(subId) + ";" + str(subNextId) + ";" + newPass + "\n")
    print("[Game] Progress autosaved!")
    print("Deciphering Emperor's message...")
    Filename = str(nextLocation) + "-" + passPhrase + ".txt"
    writeFile(Filename, cipher(cipheredMessage))
    print("Looks like I've got now the plain version copy of the Emperor's message.")
    print("Time to leave...")
    print("Travel ending.")
main()