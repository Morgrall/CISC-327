isPrivileged = True

def Main():
    while True:
        command = input()
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
    entered = input("What account are you logging in too")
    return entered

def ReadAccounts():
    accountsFile = open(str(sys.argv[0]))
    print(file.read())



if __name__ == "__Main__":
    main()
