print("Program starting.\n")
print("Insert two integers")
firstint = int(input("Insert first integer: "))
secondint = int(input("Insert second integer: "))
print("Comparing inserted integers.")
if firstint == secondint:
    print("Integers are the same")
elif firstint > secondint:
    print("First integer is greater")
elif firstint < secondint:
    print("Second integer is greater")
print()
print("Adding integers together")
sum_value = firstint + secondint
print(f"{firstint} + {secondint} = {sum_value}")
print("Checking the parity of the sum...")
if sum_value % 2 == 0:
    print("Sum is even")
else:
    print("Sum is odd")
print("Program ending.")

