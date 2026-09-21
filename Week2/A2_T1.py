print("Program starting.")
name = input("What is your name: ")
float_num = float(input("Enter a floating point number: "))
float_num_second = float(input("Enter second floating point number: "))
print(name, "you gave numbers", float_num, "and", float_num_second)
float_final = float_num * float_num_second
print("Multiplying first and second number will result in product", round(float_final, 2))
print("Program ending.")