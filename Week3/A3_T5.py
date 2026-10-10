print("Program starting.\n")
print("Options:")
print("1 - Celsius to Fahrenheit")
print("2 - Fahrenheit to Celsius")
print("0 - Exit")
choice = input("Your choice: ")

if choice == "1":
    celsius = int(input("Insert the amount of Celsius: "))
    fahrenheit = celsius * 1.8 + 32
    print(f"{celsius} °C equals to {fahrenheit} °F")
elif choice == "2":
    fahrenheit = int(input("Insert the amount of Fahrenheit: "))
    celsius = (fahrenheit - 32) / 1.8
    print(f"{fahrenheit} °F equals to {celsius} °C")
elif choice == "0":
    print("Exiting...")
else:
    print("Unknown option.")
print()
print("Program ending.")