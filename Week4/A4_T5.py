print("Program starting.\n")
starting_point = int(input("Insert starting point: "))
stopping_point = int(input("Insert stopping point: "))
inspection_point = int(input("Insert inspection point: "))
print()
if starting_point >= stopping_point:
    print("Starting point value must be less than stopping point value.")
    if not (starting_point <= inspection_point <= stopping_point):
        print("Inspection value must be within the range of start and stop.")
else:
    print("First loop-inspection with break:")
    for n in range(int(starting_point), int(inspection_point)):
        print(f"{n}", end=" " if int(starting_point) < int(inspection_point) else "\n")
    print()
    print("Second loop-inspection with continue:")
    for i in range(int(starting_point), int(stopping_point)):
        if i == int(inspection_point):
            continue
        print(f"{i}", end=" " if int(starting_point) < int(stopping_point) else "\n")
print("\nProgram ending.")
