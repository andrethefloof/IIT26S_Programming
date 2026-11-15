def main():
    print("Program is starting...")
    print("Welcome to the Wattage Calculator!")
    print("Select an option:")
    print("1 - Convert to wattage.")
    print("2 - Convert to kilowatts.")
    print ("3 - Show resistance.")
    print("0 - Exit.")
    choiceinput()
    return None
def wattagecalc():
    voltage = float(input("Enter voltage (in volts): "))
    current = float(input("Enter current (in amperes): "))
    wattage = voltage * current
    print(f"The calculated wattage is: {wattage} watts") 
    resistance = voltage / current
    filewrite(current, voltage, wattage, resistance)
def showresistance():
    voltage = float(input("Enter voltage (in volts): "))
    current = float(input("Enter current (in amperes): "))
    if current == 0:
        print("Current cannot be zero for resistance calculation.")
        return
    resistance = voltage / current
    print(f"The calculated resistance is: {resistance} ohms")
    wattage = voltage * current
    filewrite(current, voltage, wattage, resistance)
def choiceinput():
    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            wattagecalc()
        elif choice == "2":
            wattage = float(input("Enter wattage (in watts): "))
            kilowatts = wattage / 1000
            print(f"The calculated kilowatts is: {kilowatts} kW")
            filewrite(None, None, wattage, None)
        elif choice == "3":
            showresistance()
        elif choice == "0":
            print("Program ending...")
            break
        else:
            print("Unknown option selected. Try Again!")
def filewrite(current, voltage, wattage, resistance):
    file = open("wattage_calculator.txt", "a")
    file.write("Wattage Calculator Log\n")
    current_value = "0" if current is None else current
    voltage_value = "0" if voltage is None else voltage
    wattage_value = "0" if wattage is None else wattage
    resistance_value = "0" if resistance is None else resistance
    file.write(
        f"Current {current_value} A, Voltage {voltage_value} V, "
        f"Wattage {wattage_value} W, Resistance {resistance_value} Ohms\n"
        )
main()