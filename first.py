attempts = 3
login = input("Enter your user:")
while attempts > 0:
    credentials = input("Enter your password:")
    if credentials == "password12345":
        print("Login was a success!")
        break
    else:
        if credentials != "password12345":
            attempts -= 1
            print(f"You have {attempts} attempts left")
if attempts == 0:
    print("Try again later.")
