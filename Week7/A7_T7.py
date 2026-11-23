CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def main():
    rotors, reflector = readconfigfile()
    enigmamachinemenu(rotors, reflector)
def enigmamachinechar(
    row: str, Rotors: list[str], Reflector: str, Positions: list[int]
):
    convrow = ""
    for character in row:
        Positions = enigmamachineposition(Positions)
        illuminated = character
        for index in range(len(Rotors)):
            rotor = Rotors[index]
            position = Positions[index]
            shift = (CHARACTERS.index(illuminated) + position) % 26
            wiredchar = rotor[shift]
            illuminated = CHARACTERS[
                (CHARACTERS.index(wiredchar) - position) % 26
            ]
        illuminated = Reflector[CHARACTERS.index(illuminated)]
        for index in range(len(Rotors) - 1, -1, -1):
            rotor = Rotors[index]
            position = Positions[index]
            shift = (CHARACTERS.index(illuminated) + position) % 26
            shiftedchar = CHARACTERS[shift]
            index = rotor.index(shiftedchar)
            illuminated = CHARACTERS[(index - position) % 26]
        print(f'Character "{character}" illuminated as "{illuminated}"')
        convrow += illuminated
    print(f'Converted row - "{convrow}".\n')
    return convrow
def enigmamachineposition(Positions: list[int]) -> list[int]:
    newpos = Positions
    newpos[2] += 1
    if newpos[2] == 26:
        newpos[2] = 0
        newpos[1] += 1
        if newpos[1] == 26:
            newpos[1] = 0
            newpos[0] = (newpos[0] + 1) % 26
    return newpos
def readconfigfile() -> tuple[list[str], str]:
    filename = input("Insert config(filename): ")
    config: list[tuple[str, str]] = []
    with open(filename, encoding="utf-8") as conffile:
        for line in conffile:
            if ":" in line:
                key, value = line.strip().split(":", 1)
                config.append((key, value.upper()))
    rotors = ["", "", ""]
    reflector = ""
    for key, value in config:
        if key == "Rotor1":
            rotors[0] = value
        elif key == "Rotor2":
            rotors[1] = value
        elif key == "Rotor3":
            rotors[2] = value
        elif key == "Reflector":
            reflector = value
    while True:
        plugs = input("Insert plugs (y/n)?: ")
        if plugs in ("n", "N", "y", "Y"):
            print("No extra plugs inserted.")
            break
    return rotors, reflector
def enigmamachinemenu(rotors: list[str], reflector: str):
    print("Enigma initialized.\n")
    while True:
        row = input("Insert row (empty stops): ")
        if row == "":
            print()
            print("Enigma closing.")
            break
        enigmamachinechar(row.upper(), rotors, reflector, [0, 0, 0])
if __name__ == "__main__":
    main()