def deposit(balance, amount):
    ''' adds balance by amount if a positive number amount is entered
        Input: 10, "20"
        Output: (30, True)

        Input: 20, "-10"
        Output: Prints out "Invalid amount"
                returns (20, False)
    '''
    # check for number input, if true cast to int
    if (not amount.isdigit()):
        print("Invalid amount")
        return balance, False
    else:
        amount = int(amount)

    # check for positive number input    
    if (amount < 0):
        print("Invalid amount")
        return balance, False

    # print success and return final balance
    print("Deposited "+ str(amount))
    return balance + amount, True

def login(pin):
    ''' attempts to log the user in to the atm
        allows user to enter a pin three times before returning False
        if the entered pin matches the argument pin,
        prints success message and return true
    '''
    triesLeft = 3
    while (triesLeft > 0):
        inputPin = input("Enter 4-digit pin: ")
        if (pin == inputPin):
            print("Logged in successfully!")
            return True
        print("Login failed")
        triesLeft -= 1
    else:
        # 3 failed attempts
        print("Too many failed attempts")
        return False


def logout(atmFileName, pin, balance, history):
    ''' saves file data to original file
        Input: string, integer, integer, list of strings
        Output: file with title atmFileName is written with inputs
    '''
    with open(atmFileName, 'w') as atmFile:
        atmFile.write(pin + "\n")
        atmFile.write(str(balance) + "\n")
        for action in history:
            atmFile.write(action + "\n")


def printHistory(history):
    ''' prints all of the past transactions
        Input: list of strings
        Output: prints out elements of input, each on their own line
    '''
    for action in history:
        print(action)


def printMenu(balance):
    ''' prints available options using a list
        Input: integer
        Output: prints:
                "\nCurrent balance: balance"
                "Please pick 1-4"
                "1. Deposit"
                "2. Withdraw"
                "3. View past transactions"
                "4. Save and log out"
    '''
    options = [
        'Deposit',
        'Withdraw',
        'View last action',
        'Log out'
    ]

    # print initial messages
    print("\nCurrent balance: $" + str(balance))
    print("Please pick 1-" + str(len(options)))

    # print the options
    i = 0
    for option in options:
        print(str(i) + ". ", end="")
        print(option, end="\n")
        i += 1


def withdraw(balance, amount):
    ''' subtracts balance by amount if the difference is at least 0
        otherwise returns original balance
        Input: 20, 10
        Output: returns (10, True)

        Input: 30, -10
        Output: prints "Not enough in balance" and returns (30, False)

        Input: 50, abc
        Output: prints "Invalid amount" and returns (50, False)
    '''
    # check for number input, if true cast to int 
    if (not amount.isdigit()):
        print("Invalid amount")
        return balance, False
    else:
      amount = int(amount)

    # check for positive number input
    diff = balance - amount
    if (diff < 0):
        print("Not enough in balance")
        return balance, False

    # print success and return final balance
    print("Withdrew: " + str(diff))
    return diff, True


def main():
    ''' Functions as an atm. Reads and writes to a file
        Enter in a pin to find your account
        Once logged in, you can deposit or withdraw
    '''

    # obtain file data
    atmFileName = input("Enter file to read: ")
    with open(atmFileName, 'r') as atmFile:
        pin = atmFile.readline().split('\n')[0]
        balance = int(atmFile.readline().split('\n')[0])
        history = atmFile.read().split('\n')

    # validate pin
    if (not login(pin)):
        return

    # print user options and handle them appropriately
    while (True):
        printMenu(balance)
        choice = int(input(">>> Your choice: "))
        if (choice == 0):
            amount = input("Deposit amount: $")
            (balance, success) = deposit(balance, amount)
            if (success):
                history.append("Deposited $" + str(amount))
        elif (choice == 1):
            amount = input("Withdraw amount: $")
            (balance, success) = withdraw(balance, amount)
            if (success):
                history.append("Withdrew $" + str(amount))
        elif (choice == 2):
            printHistory(history)
        elif (choice == 3):
            logout(atmFileName, pin, balance, history)
            print("Thank you for using ATM!")
            break
        else:
            print("Invalid choice")
