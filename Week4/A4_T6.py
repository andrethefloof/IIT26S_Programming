print("Program starting.\n")
integer = int(input("Insert a positive integer: "))
collatz = integer
seq = str(collatz)
steps = 0
while collatz > 1:
    if collatz % 2 == 0:
        collatz = collatz // 2
    else:
        collatz = 3 * collatz + 1
    seq += "->" + str(collatz)
    steps += 1
print(f"{seq}", end ="\n")
print(f"Sequence had {steps} total steps.")
print("\nProgram ending.")