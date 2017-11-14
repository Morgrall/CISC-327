import sys

isPrivileged = False
Accounts = [] #Contains a series of 2-value arrays, where the first is the account number, and the second the amount withdrawn during the current session
transactionFile = []

def main():
    global Accounts
    Accounts = ReadAccounts()
    Login()
    while True:
        print("What transaction would you like to perform?")
        print("Available Transactions:")
        print("Withdraw")
        print("Deposit")
        print("Transfer")
        if isPrivileged:
            print("CreateAcct")
            print("DeleteAcct")
        print("Logout")
        print()
        command = input("Please enter a command: ")
        if command.upper() == "LOGOUT":
            logout()
            break
        elif command.upper() == "CREATEACCT":
            if isPrivileged:
                CreateAccount()
            else:
                print("Must be logged in as an agent to create an account")
        elif command.upper() == "DELETEACCT":
            if isPrivileged:
                DeleteAccount()
            else:
                print("Must be logged in as an agent to create an account")
        elif command.upper() == "WITHDRAW":
            Withdraw()
        elif command.upper() == "DEPOSIT":
            Deposit()
        elif command.upper() == "TRANSFER":
            Transfer()
    return

def Login():
    #Logs into ATM or agent account.  Takes no arguments, returns a Boolean relating to the account
    #Input: ATM or AGENT
    #Output: Stdout error messages
    global isPrivileged
    entered = input("What account are you logging in to (ATM/AGENT): ")
    if entered.upper() == "AGENT":
        isPrivileged = True
    elif entered.upper() == "ATM":
        isPrivileged = False
    else:
        print("please enter: ATM or AGENT")
        Login()

def ReadAccounts():
    #Reads the Accounts.txt file into the global Accounts array
    #Input: None
    #Output: None
    Accounts = []
    accountsFile = open('Accounts.txt', 'r')
    lines = accountsFile.read().split("\n")
    for line in lines:
        line = int(line)
        account = [line, 0]
        Accounts.append(account)
    accountsFile.close()
    return Accounts

def acctNumIn(prompt):
    #Prompts the user to enter an account number, checks the input formatting
    #Input: a 7-digit number
    #Output: Stdout error messages
    while True:
        acctNum = input(prompt)
        if len(acctNum) != 7:
            print("Please ensure that you have entered a 7-digit number.")
        elif acctNum[0] == 0:
            print("Account numbers cannot begin with zero. Please check your number and try again.")
        else:
            try:
                acctNum = int(acctNum)
            except ValueError:
                print("Please ensure that you have entered a 7-digit number.")
                return acctNumIn(prompt) 
            return acctNum

def acctNameIn(prompt):
    #Prompts the user to enter an account number, checks the input formatting
    #Input: an alphanumeric string between 3-30 characters (inclusive)
    #Output: Stdout error messages
    while True:
        acctName = input(prompt)
        if len(acctName) > 30:
            print("Account names cannot exceed 30 characters")
        elif len(acctName) < 3:
            print("Account names must be at least 3 characters")
        elif acctName[0] == ' ':
            print("Account names cannot begin with a space. Please check your number and try again.")
        elif acctName.replace(" ", "").isalnum() != True:
            print("Account names must be comprised of alphanumeric characters.")
        else:
            return acctName

def amountIn(prompt):
    #Prompts the user to enter an account number, checks the formatting 
    #Input: a 1-8 digit number
    #Output: Stdout error messages
    while True:
        amount = input(prompt)
        if len(amount) > 8:
            print("Amount too large.  Please try again.")
        elif amount[0] == '0':
            print("Amount cannot begin with a zero. Please try again.")
        else:
            try:
                amount = int(amount)
            except ValueError:
                print("Please ensure that you have entered a number.")
                return amountIn(prompt)
            return amount

def CreateAccount():
    #Generates a new account, Only available in AGENT mode
    #Input: Account number, account name
    #Output: Transaction description to the transactionFile array, stdout error messages
    global Accounts
    global transactionFile
    accountNumber = acctNumIn("Please enter an account number: ")
    if accountExists(accountNumber):
        print("Account already exists")
        CreateAccount()
    else:
        accountName = acctNameIn("Please enter an account name: ")
    output = "NEW "
    output+=str(accountNumber)
    output+=" 000 0000000 "
    output+=accountName
    transactionFile.append(output)

def DeleteAccount():
    #Deletes an account. Only available in AGENT mode
    #Input: Account number, account name
    #Output: Transaction description to the transactionFile array, stdout error messages
    global Accounts
    global transactionFile
    accountNumber = acctNumIn("Please enter an account number: ")
    if accountExists(accountNumber):
        accountName = acctNameIn("Please enter an account name: ")
    else:
        print("Account does not exist")
        DeleteAccount()
    index = accountIndex(accountNumber)
    del Accounts[index]
    output = "DEL "
    output+=str(accountNumber)
    output+=" 000 0000000 "
    output+=accountName

def Deposit():
    #Deposits a user-input amount into a specified account
    #Input: Account number, amount to deposit
    #Output: Transaction description to the transactionFile array, stdout error messages
    global Accounts
    global transactionFile
    accountNumber = acctNumIn("Please enter an account number: ")
    if accountExists(accountNumber):
        while True:
            depositAmount = amountIn("Please enter an amount to deposit: ")
            if isPrivileged and depositAmount > 99999999:
                print("You can not deposit over $999999.99 in AGENT mode")
            elif (isPrivileged == False) and depositAmount > 100000:
                print("You can not deposit over $1000.00 in AGENT mode")
            else:
                output = "DEP "
                output+=str(accountNumber)
                output+=" "
                output+=str(depositAmount)
                output+=" 0000000 ***"
                transactionFile.append(output)
                break
    else:
        print("Account does not exist")
        Deposit()
        
def Withdraw():
    #Withdraws a user-input amount from a specified account. Withdraw limit changes based on transaction mode (ATM or AGENT).
    #Input: Account number, amount to withdraw
    #Output: Transaction description to the transactionFile array, stdout error messages
    global Accounts
    global transactionFile
    accountNumber = acctNumIn("Please enter an account number: ")
    if accountExists(accountNumber):
        index = accountIndex(accountNumber)
        withdrawAmount = amountIn("Please enter an amount to withdraw: ")
        if isPrivileged and withdrawAmount > 99999999:
            print("You can not withdraw over $999999.99 in AGENT mode")
        elif (isPrivileged == False) and (Accounts[index][1]+withdrawAmount) > 100000:
            print("You cannot withdraw more than $1000 in a single session")
        elif (isPrivileged == False) and withdrawAmount > 100000:
            print("You can not withdraw over $1000.00 in AGENT mode")
        else:
            output = "WDR "
            output+=str(accountNumber)
            output+=" "
            output+=str(withdrawAmount)
            output+=" 0000000 ***"
            Accounts[index][1] += withdrawAmount
            transactionFile.append(output) 
    else:
        print("Account does not exist")
        Withdraw()
    
def Transfer():
    #Transfers a user-input amount from one account to another.  Transfer limit based on transaction mode (ATM or AGENT)
    #Input: Two account numbers, amount to transfer
    #Output: Transaction description to the transactionFile array, stdout error messages
    global Accounts
    global transactionFile
    accountNumber = acctNumIn("Please enter an account number to transfer from: ")
    if accountExists(accountNumber):
        while True:
            transferAmount = amountIn("Please enter an amount to Transfer: ")
            if isPrivileged and transferAmount > 99999999:
                print("You can not transfer over $999999.99 in AGENT mode")
            elif (isPrivileged == False) and transferAmount > 100000:
                print("You can not transfer over $1000.00 in AGENT mode")
            else:
                while True:
                    secondAccountNumber = acctNumIn("Please enter an account number to transfer to: ")
                    if accountExists(secondAccountNumber):
                        output = "XFR "
                        output+=str(accountNumber)
                        output+=" "
                        output+=str(transferAmount)
                        output+=" "
                        output+=str(secondAccountNumber)
                        output+=" ***"
                        transactionFile.append(output)
                        break
                    else:
                        print("please enter a valid account")
            break
    else:
        print("Account doesn't exist")
        Deposit()

def accountExists(accountNum):
    #Checks to see if the provided account number exists.
    #Input: None
    #Output: None
    global Accounts
    for i in Accounts:
        if i[0] == accountNum:
            return True
    return False

def accountIndex(accountNum):
    #Returns the index of an account, given its account number.
    #Inputs: None
    #Outputs: None
    global Accounts
    index = 0
    for i in Accounts:
        if i[0] == accountNum:
            return index
        else:
            index += 1


def logout():
    #Ends the session, and writes each element of the transactionFile array into the transaction summary file
    #Input: None
    #Output: Transaction Summary File
    transactionSummary = open('transactionSummaryFile.txt', 'w')
    for i in range(0, len(transactionFile) - 1):
        transactionSummary.write(transactionFile[i]+'\n')
    transactionSummary.write(transactionFile[len(transactionFile)-1])
    transactionSummary.close()
    return


if __name__ == "__main__":
    main()
