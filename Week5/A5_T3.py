def main():
    print("Program starting.")
    name = askName()
    greetUser(name)
    print("Program ending.")
    return None
def askName():
    name = input("Insert your name: ")
    return name
def greetUser(Pname):
    print(f"Hello {Pname}!")
    return None
main()