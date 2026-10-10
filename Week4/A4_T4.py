print("Program starting.\n")
w_count = 0
c_count = 0
while True:
    word = input("Insert word (empty stops): ")
    if word == "":
        break
    w_count += 1
    c_count += len(word)
print("\nYou inserted: ")
print(f"- {w_count} words")
print(f"- {c_count} characters\n")
print("Program ending.")