def main():
    print("Program starting.")
    print("Collect positive integers.")
    integers = integercollect()
    outputresults(integers)
    return None
def integercollect():
    integers: list[int] = []
    while True:
        integer = int(input("Insert positive integer (negative stops): "))
        if integer < 0:
            break
        integers.append(integer)
    print("Stopped collecting positive integers.")
    return integers
def outputresults(integers: list[int]):
    print(f"Displaying {len(integers)} integers:")
    index = 0
    while index < len(integers):
        integer = integers[index]
        print(f"Index {index} => Ordinal {index + 1} => Integer {integer}")
        index += 1
    print("Program ending.")
    return None
if __name__ == "__main__":
    main()