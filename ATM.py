Id = [0] * 10
Money = [0.0] * 10

def ValidateUserId(UserId):
    if UserId < 0 or UserId > 10:
        return False
    return True

def SignIn():
    UserId = int(input("Please enter the user id:\n"))
    
    if ValidateUserId(UserId):
        if UserId == Id[UserId - 1]:
            print("The user Id already exists")
        else:
            Id[UserId - 1] = UserId
    else:
        print("Please enter a correct user id")

def MoneyMenu(UserId):
    print("Enter 1 to withdraw money")
    print("Enter 2 to deposit money")
    print("Enter 3 to request the balance")
    print("Enter 4 to go back to the main menu")
    
    Amounts = 0
    Choice = int(input("Enter your choice:\n"))
    Note = [5000, 1000, 500, 100, 50, 20, 10]
    
    if Choice == 1:
        while True:
            Amounts = float(input("Enter withdrawal amount:\n"))
            Tempo = int(Amounts)
            if Tempo % 10 == 0 and Amounts > 0 and Tempo == Amounts:
                break
            else:
                print("Invalid amount. Please enter a multiple of 10")
        
        if Amounts <= Money[UserId - 1]:
            Money[UserId - 1] -= Amounts
            for note in Note:
                dem = Amounts // note
                if dem > 0:
                    print(f"Denomination of {note}: {int(dem)}")
                Amounts -= dem * note
        else:
            print("The balance is insufficient")
    
    elif Choice == 2:
        invalids = True
        while invalids:
            try:
                Amounts = float(input("Please enter the amount to deposit:\n"))
                if Amounts <= 0:
                    print("Please enter a positive amount")
                else:
                    invalids = False
            except ValueError:
                print("Error: Invalid input. Please enter a valid number")
        Money[UserId - 1] += Amounts
    
    elif Choice == 3:
        print(f"User ID {UserId} has an amount of {Money[UserId - 1]}")
    
    elif Choice == 4:
        return False
    
    else:
        print("Please enter the correct choice")
    
    return True

def log_In():
    UserId = int(input("Please enter the user id:\n"))
    
    if ValidateUserId(UserId) and Id[UserId - 1] != 0:
        run = True
        while run:
            run = MoneyMenu(UserId)
    else:
        print("User has entered an invalid user id")

def DisplayMenu():
    print("Main menu:")
    print("Enter 1 to create a bank account using user ID")
    print("Enter 2 to log in using user ID")
    print("Enter 3 to quit the bank")
    
    Choice = int(input("Enter your choice:\n"))
    
    if Choice == 1:
        SignIn()
    elif Choice == 2:
        log_In()
    elif Choice == 3:
        return False
    else:
        print("Please enter the correct number from the menu")
    
    return True

def main():
    represent = True
    while represent:
        represent = DisplayMenu()

if __name__ == "__main__":
    main()
