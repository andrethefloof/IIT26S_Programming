print("Program starting.\n")
starting = int(input("Insert starting value: "))
stopping = int(input("Insert stopping value: "))
print()
print("Starting while-loop:")
while starting <= stopping:
    print(starting, end=" " if starting < stopping else "\n")
    starting += 1
print()
print("Program ending.")