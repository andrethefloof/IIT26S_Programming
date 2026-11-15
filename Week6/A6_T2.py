def writeFile(fname, lname, filename):
    filehandler = open(filename, 'w', encoding='utf-8')
    filehandler.write(fname + '\n')
    filehandler.write(lname + '\n')
    filehandler.close()

def main():
    print("Program starting...")
    fname = input("Insert first name: ")
    lname = input("Insert last name: ")
    filename = input("Insert filename: ")
    writeFile(fname, lname, filename)
    print("Program ending.")
    return None
main()