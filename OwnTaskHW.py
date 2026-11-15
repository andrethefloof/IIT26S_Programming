def main():
    print("Program starting...")
    print("Welcome to the Steps and Speed Calculator")
    print("Please select from the following options:")
    print("1 - Enter the name.")
    print("2 - Enter distance in meters.")
    print("3 - Show number of steps.")
    print("4 - Show average speed.")
    print("5 - Convert distance to kilometers.")
    print("6 - Show all information.")
    print("0 - Exit")
    ChoiceInput()
    return None
def ChoiceInput():
    meters = 0
    name = "Anonymous"
    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter your name: ")
            print(f"Welcome, {name}!")
        elif choice == "2":
            meters = float(input("Enter distance in meters: "))
            print(f"Distance in meters: {meters} m")
        elif choice == "3":
            stepcalculation(meters)
        elif choice == "4":
            speedaverage(meters)
        elif choice == "5":
            convtokm(meters)
        elif choice == "6":
            print(f"Name: {name}")
            print(f"Distance in meters: {meters} m")
            stepcalculation(meters)
            speedaverage(meters)
            convtokm(meters)
        elif choice == "0":
            print("Program ending...")
            break
        else:
            print("Unknown option selected. Try Again!")
def stepcalculation(meters):
    steps = meters * 1.31234
    print(f"Number of steps: {steps}")
def speedaverage(meters):
    time = float(input("Enter time in seconds: "))
    if time <= 0:
        print("Time must be greater than zero.")
        return
    speed = meters / time
    print(f"Average speed: {speed} m/s")
def convtokm(meters):
    kilometers = meters / 1000
    print(f"Distance in kilometers: {kilometers} km")
main()