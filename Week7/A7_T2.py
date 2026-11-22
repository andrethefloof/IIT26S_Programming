SEPARATOR = ","
def main():
    print("Program starting.")
    integers, invalid = commasepint()
    for inv in invalid:
        print(f"Invalid value '{inv}' detected.")
    if integers == []:
        print("No values to analyse.")
    else:
        print(f"There are {len(integers)} integers in the list.")
        total_sum, parity = sumandparity(integers)
        print(f"Sum of the integers is {total_sum} and it's {parity}")
    print("Program ending.")
    return None
def commasepint():
    integers: list[int] = []
    invalid: list[str] = []
    values = input("Insert comma separated integers: ").split(SEPARATOR)
    for value in values:
        value = value.strip()
        if value.lstrip('-').isdigit():
            integers.append(int(value))
        else:
            invalid.append(value)
    return integers, invalid
def sumandparity(integers: list[int]):
    total_sum = sum(integers)
    if total_sum % 2 == 0:
        parity = "even"
    else:
        parity = "odd"
    return total_sum, parity
if __name__ == "__main__":
    main()