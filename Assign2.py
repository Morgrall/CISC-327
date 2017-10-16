import sys

isPrivileged = True
Accounts = []
transactionFile = []

def main():
    global Accounts
    Accounts = ReadAccounts()
    while True:
        command = input("Please enter a command")
        if command.upper() == "LOGIN":
            global isPrivileged
            isPrivileged = Login()
        elif command.upper() == "LOGOUT":
            Logout()
        elif command.upper() == "CREATEACCT":
            CreateAccount()
        elif command.upper() == "DELETEACCT":
            DeleteAccount()
        elif command.upper() == "WITHDRAW":
            Withdraw()
        elif command.upper() == "DEPOSIT":
            Deposit()
        elif command.upper() == "TRANSFER":
            Transfer()

def Login():
    entered = input("What account are you logging in too. (ATM/AGENT)")
    if entered.upper == "ATM" or entered.upper == "AGENT":
        return entered
    else:
        print("please enter: ATM or AGENT")
        return Login()

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

def DeleteAccount
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
        

def accountExists(accountNum):
    global Accounts
    for i in Accounts:
        if i == accountNum:
            return True
    return False


if __name__ == "__main__":
    main()
