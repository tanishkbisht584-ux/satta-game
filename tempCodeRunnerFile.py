def deposit():
    while True:
        amount = input("What would you like to deposite? ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Ammount must be greater than 0.")
        else:
            print("Please enter a valid number.")
    return amount

deposit()
