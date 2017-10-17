import sys

isPrivileged = False
Accounts = []
transactionFile = []

def main():
    global Accounts
    Accounts = ReadAccounts()
    Login()
    while True:
        command = input("Please enter a command")
        if command.upper() == "LOGOUT":
            Logout()
        elif command.upper() == "CREATEACCT":
            if isPrivileged():
                CreateAccount()
            else:
                print("Must be logged in as an agent to create an account")
        elif command.upper() == "DELETEACCT":
            if isPrivileged():
                DeleteAccount()
            else:
                print("Must be logged in as an agent to create an account")
        elif command.upper() == "WITHDRAW":
            Withdraw()
        elif command.upper() == "DEPOSIT":
            Deposit()
        elif command.upper() == "TRANSFER":
            Transfer()

def Login():
    global isPrivileged
    entered = input("What account are you logging in too. (ATM/AGENT)")
    if entered.upper == "AGENT":
        isPrivileged = True
    elif entered.upper == "ATM":
        isPrivileged = False
    else:
        print("please enter: ATM or AGENT")
        Login()

def ReadAccounts():
    Accounts = []
    accountsFile = open(str(sys.argv[1]))
    content = accountsFile.readlines()
    content = [x.strip() for x in content]
    return Accounts

def CreateAccount():
    global Accounts
    global transactionFile
    accountNumber = input("Please enter an account number")
    if accountExists():
        print("Account already exists")
        CreateAccount()
    else:
        accountName = input("Please enter an account name")
    output = "NEW "
    output+=accountNumber
    output+=" 000 0000000 "
    output+=accountName
    transactionFile.append(output)

def DeleteAccount():
    global Accounts
    global transactionFile
    accountNumber = input("Please enter an account number")
    if accountExists():
        accountName = input("Please enter an account name")
    else:
        print("Account doesn't exist")
        CreateAccount()
    Accounts.remove(accountNumber)
    output = "DEL "
    output+=accountNumber
    output+=" 000 0000000 "
    output+=accountName

def Deposit():
    global Accounts
    global transactionFile
    accountNumber = input("Please enter an account number")
    if accountExists():
        while True
            depositAmount = input("Please enter an amount to deposit")
            if isPrivileged:
                if int(depositAmount) > 99999999:
                    print("You can not withdraw over $999999.99 in AGENT mode")
                else:
                    output = "DEP "
                    output+=accountNumber
                    output+=depositAmount
                    output+=" 0000000 ***"
                    transactionFile.append(output)
                    break
            else:
                if int(depositAmount) > 100000:
                    print("You can not withdraw over $1000.00 in ATM mode")
                else:
                    output = "DEP "
                    output+=accountNumber
                    output+=" 000 0000000 "
                    output+=accountName
                    transactionFile.append(output)
                    break
    else:
        print("Account doesn't exist")
        Deposit()

def logout():
    pass
#TODO
def Withdraw():
    global Accounts
    global transactionFile
    accountNumber = input("Please enter an amount to withdraw")
    if accountExists():
        withdrawAmount = input("Please enter an account name")
        if isPrivileged
    else:
        print("Account doesn't exist")
        Withdraw()
    
def Transfer():
    global Accounts
    global transactionFile
    accountNumber = input("Please enter an account number to transfer from")
    if accountExists():
        while True:
            depositAmount = input("Please enter an amount to Transfer")
            if isPrivileged:
                if int(depositAmount) > 99999999:
                    print("You can not withdraw over $999999.99 in AGENT mode")
                else:
                    while True
                        secondAccountNumber = input("Please enter an account number to transfer to")
                        if accountExists():
                            output = "XFR "
                            output+=accountNumber
                            output+=depositAmount
                            output+=" 0000000 ***"
                            transactionFile.append(output)
                            break
                        else:
                            print("please enter a valid account")
                    break
            else:
                if int(depositAmount) > 100000:
                    print("You can not withdraw over $1000.00 in ATM mode")
                else:
                    while True
                        secondAccountNumber = input("Please enter an account number to transfer to")
                        if accountExists():
                            output = "XFR "
                            output+=accountNumber
                            output+=depositAmount
                            output+=" 0000000 ***"
                            transactionFile.append(output)
                            break
                        else:
                            print("please enter a valid account")
                    break
    else:
        print("Account doesn't exist")
        Deposit()

def accountExists(accountNum):
    global Accounts
    for i in Accounts:
        if i == accountNum:
            return True
    return False


if __name__ == "__main__":
    main()
