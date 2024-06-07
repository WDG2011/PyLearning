password = "python"
attempts = 0

while attempts < 3:
    userinput = input("Enter your password: ")
    if userinput == password:
        print("Welcome!")
        break
    else:
        print("Password incorrect, please try again!")
        attempts += 1

if attempts == 3:
    print("You have been locked out. BOOHOO!")
