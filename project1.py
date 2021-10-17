# Code  by: Alejandro A. Perez Pabon
NameAccount = input("Please enter the name of your account: ")
StartingBalance = float(input("Please enter the starting balance: "))
Balance = StartingBalance
op1, op2F, op2T, totalD, totalWF, totalWT, totalF = 0, 0, 0, 0, 0, 0, 0
print("Account: ", NameAccount, "\n" "Balance: ", StartingBalance)
option = None

while option != 3:
    print("You may:")
    print("1) Deposit some funds")
    print("2) Withdraw some funds")
    print("3) Quit")
    option = int(input("Select your option: "))
    if option == 1:
        print("Amount deposit ")
        a = float(input(": "))
        Balance += a
        print("Account: ", NameAccount, "\nBalance: ", Balance)
        op1 += 1
        totalD += a
    if option == 2:
        print("Amount withdraw")
        c = float(input(": "))
        y = Balance - c
        if y < 0:
            f = 5.0
            Balance = float(Balance - f)
            print("Insufficient funds. For your convenience, an overdraft fee of $5 is being deducted from your balance. Have a nice day.")
            print("Account: ", NameAccount, "\nBalance: ", Balance)
            op2F += 1
            totalWF += c
            totalF += f
        else:
            Balance -= c
            print("Account: ", NameAccount, "\nBalance: ", y)
            op2T += 1
            totalWT += c
    if option == 3:
        print("Final statement:")
        print("Account: ", NameAccount, "\nBalance: ", Balance)
        print(op1, "deposits totaling", totalD)
        print(op2T, "withdrawals totaling", totalWT)
        print(op2F, "bad withdrawals totaling", totalWF)
        print(op2F, "fees totaling", totalF)
