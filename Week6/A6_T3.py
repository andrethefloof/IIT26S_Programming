def readFile(srcfile):
    filehandlerread = open(srcfile, 'r', encoding='utf-8')
    Content = ''
    Row = filehandlerread.readline()
    while Row != '':
        Content += Row
        Row = filehandlerread.readline()
    filehandlerread.close()
    return Content
def writeFile(destfile, Content):
    filehandlerwrite = open(destfile, 'w', encoding='utf-8')
    filehandlerwrite.write(Content)
    filehandlerwrite.close()
def main():
    print("Program starting...")
    print("This program can copy a file")
    srcfile = input("Insert source filename: ")
    destfile = input("Insert destination filename: ")
    print(f"Reading file '{srcfile}' content")
    print("File content read in memory.")
    Content = readFile(srcfile)
    print(f"Writing content into file '{destfile}'.")
    writeFile(destfile, Content)
    print("Copying operation complete.")
    print("Program ending.")
    return None
main()