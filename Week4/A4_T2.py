print("Program starting.\n")
starting = int(input("Insert starting value: "))
stopping = int(input("Insert stopping value: ")) + 1
print("\nStarting for-loop:")
for n in range(starting, stopping):
    print(n, end=" " if n < stopping - 1 else "\n")
print()
print("Program ending.")