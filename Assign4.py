import sys

accounts = []
transactions = []
newAccounts = []

def main():
    global accounts
    accounts = readArray('masterAccountsFile.txt')
    global transactions
    transactions = readArray('transactionSummaryFile.txt')
    for transaction in transactions:
    #Main backend loop
        transArr = makeTransArr(transaction)
        if transArr[0] == "WDR":
            withdraw(transArr[1:])
        elif  transArr[0] == "DEP":
            deposit(transArr[1:])
        elif transArr[0] == "XFR":
            transfer(transArr[1:])
        elif transArr[0] == "NEW":
            newAcct(transArr[1:])
        elif transArr[0] == "DEL":
            delAcct(transArr[1:])
        else:
            print("Something went wrong.")
    
    accounts = mergeNewAccounts()
    writeMasterAccounts()
    writeValidAccounts()
    writeMergedTransactionFile()




def readArray(path):
    #returns an array where each element is a single line of the file at the given path
    array = []
    file = open(path, 'r')
    lines = file.read().split("\n")
    for line in lines:
        array.append(line)
    file.close()
    return array


def findAccount(number):
    #returns index of the specified account within the accounts array
    accountNum = accounts[0][:7]
    if number == accountNum:
        return 0
    else:
        i=1
        while number != accountNum:
            accountNum = accounts[i][:7]
            i+=1
        return i
    return
    

def makeTransArr(transaction):
    #breaks a transaction string into an array mapped to [code, account # to, amount, account # from, account name]
    arr = [transaction[:3]] #transaction code
    arr.append(transaction[4:11]) #account # to
    i = 12
    while transaction[i] != " ":
        i+=1
    arr.append(transaction[12:i]) #amount
    j = i+1 #start of account # from
    while transaction[j] != " ":
        j+=1
    arr.append(transaction[i+1:j]) #account # from
    arr.append(transaction[j:]) #account name
    return arr


def updateAccount(index, balance, name):
    #given an account to change and a new balance, updates that account's balance
    accounts[index] = accounts[index][:7] + " " + str(balance) + str(name)


def withdraw(arr):
    #given a transaction array sans transaction code, removes the specified amount from the specified account
    accountIndex = findAccount(arr[0])
    account = accounts[accountIndex]
    i = 8
    while account[i] != " ": #finds index of end of account balance
        i+=1
    balance = int(account[7:i]) - int(arr[1])
    updateAccount(accountIndex, balance, account[i:])


def deposit(arr):
    #given a transaction array sans transaction code, adds the specified amount to the specified account
    accountIndex = findAccount(arr[0])
    account = accounts[accountIndex]
    i = 8
    while account[i] != " ": #finds index of end of account balance
        i+=1
    balance = int(account[7:i]) + int(arr[1])
    updateAccount(accountIndex, balance, account[i:])


def transfer(arr):
    #given a transaction array sans transaction code, removes the specified amount from the specified account and adds it to the other given account
    withdraw(arr)
    #pull account to number to use with deposit()
    hold = arr[0]
    arr[0] = arr[2]
    arr[2] = hold
    deposit(arr)
    
        
def newAcct(arr):
    #given a transaction array sans transaction code, creates a new account with the given number and name
    acctStr = arr[0]+ ' 000' + arr[3]
    newAccounts.append(acctStr)
    

def delAcct(arr):
    #given a transaction array sans transaction code, deletes the specified account
    index = findAccount(arr[0])
    del accounts[index]
    

def mergeNewAccounts():
    #at the end of a backend session, sorts the newly created accounts into the existing accounts array
    for newAccount in newAccounts:
        accountNum = newAccount[:7]
        if accountNum < accounts[0][4:11]:
            accounts.insert(0, newAccount)
            break
        i=0
        while i < len(accounts) and accountNum > accounts[i][4:11]:
            i+=1
        accounts.insert(i, newAccount)
    return accounts


def writeMasterAccounts():
    #writes each element of the accounts array into the master accounts file
    masterAccounts = open('masterAccountsFile.txt', 'w')
    print(accounts)
    for i in range(0, len(accounts) - 1):
        masterAccounts.write(accounts[i]+'\n')
    masterAccounts.write(accounts[len(accounts)-1])
    masterAccounts.close()
    

def writeValidAccounts():
    #writes just the account number from every element of the accounts array to the valid accounts file
    validAccounts = open('Accounts.txt', 'w')
    for i in range(0, len(accounts) - 1):
        validAccounts.write(accounts[i][:7]+'\n')
    validAccounts.write(accounts[len(accounts)-1][:7])
    validAccounts.close()


def writeMergedTransactionFile():
    #appends day's transactions to the merged transaction file
    transactionSummary = open('mergedTransactionFile.txt', 'a')
    for elem in transactions:
        transactionSummary.write(elem+'\n')
    transactionSummary.close()


        

main()





