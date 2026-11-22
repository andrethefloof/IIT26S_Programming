WEEKDAYS: tuple[str] = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
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
    print("Electricity usage:")
    for time in PTimestamps:
        total = time.consumption * time.price
        print(f"- {time.weekday} {time.hour}, price {time.price:.2f}, consumption {time.consumption:.2f} kWh, total {total:.2f} €")
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