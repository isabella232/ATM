def deposit(balance, amount):
    ''' adds balance by amount if a positive number amount is entered
        Input: 10, "20"
        Output: (30, True)

        Input: 20, "-10"
        Output: Prints out "Invalid amount"
                returns (20, False)
    '''
    # check for positive number input

    # print success and return final balance


def login(pin):
    ''' attempts to log the user in to the atm
        allows user to enter a pin three times before returning False
        if the entered pin matches the argument pin,
        prints success message and return true
    '''


def logout(atmFileName, pin, balance, history):
    ''' saves file data to original file
        Input: string, integer, integer, list of strings
        Output: file with title atmFileName is written with inputs
    '''


def printHistory(history):
    ''' prints all of the past transactions
        Input: list of strings
        Output: prints out elements of input, each on their own line
    '''

        
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
    # print initial messages

    # print the options

        
def withdraw(balance, amount):
    ''' subtracts balance by amount if the difference is at least 0
        otherwise returns original balance
        Input: 20, "10"
        Output: returns (10, True)

        Input: 30, "-10"
        Output: prints "Not enough in balance" and returns (30, False)

        Input: 50, "abc"
        Output: prints "Invalid amount" and returns (50, False)
    '''
    # check for number input

    # check for positive number input

    # print success and return final balance

                  
def main():
    ''' Functions as an atm. Reads and writes to a file
        Enter in a pin to find your account
        Once logged in, you can deposit or withdraw
    '''

    # obtain file data
    # This code is used to remove the trailing newline
    # .readline().split('\n')[0]
    # .readline().split('\n')[0])
    # .read().split('\n')

    # validate pin

    # print user options and handle them appropriately
