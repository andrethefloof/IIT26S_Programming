WEEKDAYS: tuple[str] = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturnday",
    "Sunday",
)
DELIMITER = ";"
class TIMESTAMP:
    weekday: str
    hour: str
    consumption: float
    price: float
def readFile(PFilename: str, PTimestamps: list[TIMESTAMP]) -> None:
    print('Reading file "{}".'.format(PFilename))
    PTimestamps.clear()
    filehandle = open(PFilename, "r", encoding="utf-8")
    lineskip = False
    for line in filehandle:
        if not lineskip:
            lineskip = True
            continue
        if line != "\n":
            Row = line.rstrip("\n")
            Columns = Row.split(DELIMITER)
            if len(Columns) >= 4:
                Timestamp = TIMESTAMP()
                Timestamp.weekday = Columns[0]
                Timestamp.hour = Columns[1]
                Timestamp.consumption = float(Columns[2])
                Timestamp.price = float(Columns[3])
                PTimestamps.append(Timestamp)
            Columns.clear()
    filehandle.close()
    return None
def displayResults(PTimestamps: list[TIMESTAMP]) -> None:
    print("Analysing timestamps.")
    print("Displaying results.")
    print("### Electricity consumption summary ###")
    consumptionday = {day: 0.0 for day in WEEKDAYS}
    costday = {day: 0.0 for day in WEEKDAYS}
    for time in PTimestamps:
        consumptionday[time.weekday] += time.consumption
        costday[time.weekday] += time.consumption * time.price
    for day in WEEKDAYS:
        print(f"- {day} usage {consumptionday[day]:.2f} kWh, "
        f"cost {costday[day]:.2f} €")
    print("### Electricity consumption summary ###")
    return None
def main() -> None:
    print("Program starting.")
    timestamps: list[TIMESTAMP] = []
    filename = input("Insert filename: ")
    readFile(filename, timestamps)
    displayResults(timestamps)
    timestamps.clear()
    print("Program ending.")
    return None
if __name__ == "__main__":
    main()