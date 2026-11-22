WEEKDAYS: tuple[str] = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
)
def readFile(PFilename: str, PRows: list[str]) -> None:
    print('Reading file "{}".'.format(PFilename))
    PRows.clear()
    filehandle = open(PFilename, "r", encoding="utf-8")
    lineskip = False
    for line in filehandle:
        if not lineskip:
            lineskip = True
            continue
        if line != "\n":
            PRows.append(line.strip("\n"))
    filehandle.close()
    return None
def analyseTimestamps(PRows: list[str], PResults: list[str]) -> None:
    print("Analysing timestamps.")
    weektime: list[int] = [0, 0, 0, 0, 0, 0, 0]
    for i in range(len(PRows)):
        for j in range(len(WEEKDAYS)):
            if PRows[i].startswith(WEEKDAYS[j]):
                weektime[j] += 1
    for i in range(len(WEEKDAYS)):
        PResults.append(f"- {WEEKDAYS[i]} {weektime[i]} stamps")
    weektime.clear()
    return None
def displayResults(PResults: list[str]) -> None:
    print("Displaying results.")
    print("### Timestamp analysis ###")
    for result in PResults:
        print(result)
    print("### Timestamp analysis ###")
    return None
def main() -> None:
    print("Program starting.")
    rows: list[str] = []
    results: list[str] = []
    filename = input("Insert filename: ")
    readFile(filename, rows)
    analyseTimestamps(rows, results)
    displayResults(results)
    rows.clear()
    results.clear()
    print("Program ending.")
    return None
if __name__ == "__main__":
    main()