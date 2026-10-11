print("Check multiplicative persistence.")
integer = int(input("Insert an integer: "))
steps = 0
while integer >= 10:
    multi = ""
    product = 1
    for digit in str(integer):
        product *= int(digit)
        if multi == "":
            multi = digit
        else:
            multi = multi + " * " + digit
    print(multi + " = " + str(product))
    integer = product
    steps += 1
print("No more steps.\n")
print(f"This program took {steps} step(s).\n")
print("Program ending.")