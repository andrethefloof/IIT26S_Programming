SEPARATOR = ";"
def readValues(filename):
    count = 0
    value_sum = 0
    greatest_value = None
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            for value in line.strip().split(SEPARATOR):
                if value.strip():
                    num = int(value.strip())
                    count += 1
                    value_sum += num
                    if greatest_value is None or num > greatest_value:
                        greatest_value = num
    return count, value_sum, greatest_value
def main():
    print("Program starting.")
    filename = input("Insert filename: ")
    value_count, value_sum, greatest_value = readValues(filename)
    average_value = value_sum / value_count
    print("#### Number analysis - START ####")
    print(f'File "{filename}" results:')
    print("Count;Sum;Greatest;Average")
    print(f"{value_count};{value_sum};{greatest_value};{average_value:.2f}")
    print()
    print("#### Number analysis - END ####")
    print("Program ending.")

main()