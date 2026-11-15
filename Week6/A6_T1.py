def readFile(filename): 
    filehandler = open(filename, 'r', encoding='utf-8')
    Content = ''
    Row = filehandler.readline()
    while Row != '':
        Content += Row
        Row = filehandler.readline()
    filehandler.close()
    return Content

def main():
    print("Program starting...")
    print("This program can read a file")
    filename = input("Insert filename: ")
    fileContent = readFile(filename)
    print(f'### START "{filename}" ###')
    print(fileContent)
    print(f'### END "{filename}" ###')
    print("Program ending.") 
    return None
main()