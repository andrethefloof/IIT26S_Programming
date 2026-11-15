def analyzeFile(srcfile):
    count = 0
    shortest_len = None
    longest_len = 0
    total_len = 0
    with open(srcfile, 'r', encoding='utf-8') as fread:
        for line in fread:
            name = line.strip()
            if name:
                name_len = len(name)
                count += 1
                total_len += name_len
                if shortest_len is None or name_len < shortest_len:
                    shortest_len = name_len
                if name_len > longest_len:
                    longest_len = name_len         
    return count, shortest_len if shortest_len is not None else 0, longest_len, total_len
def main():
    print("Program starting.")
    print("This program analyses a list of names from a file.")
    filename = input("Insert filename: ")
    print(f'Readin names from "{filename}"')
    print("Analysing names...")
    count, shortest, longest, total_len = analyzeFile(filename)
    avg_len = total_len / count if count > 0 else 0
    print("Analysis complete!")
    print("### REPORT BEGIN ###")
    print(f"Name count: {count}")
    print(f"Shortest name: {shortest}")
    print(f"Longest name: {longest}")
    print(f"Average name length: {avg_len:.2f}")

main()