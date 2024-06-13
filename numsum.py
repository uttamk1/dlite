pin = 1234
atmbalance = 10000000
userbalance = 345000
flag = 0

def withdraw(withdrawal_amt):
    global atmbalance, userbalance
    if withdrawal_amt % 100 == 0:
        if (userbalance >= withdrawal_amt) and (atmbalance >= withdrawal_amt):
            atmbalance -= withdrawal_amt
            userbalance -= withdrawal_amt
            print("Amount withdrawn successfully")
        else:
            print("Insufficient balance")
    else:
        print("Try again")

def deposit(amt):
    global atmbalance, userbalance
    if amt % 100 == 0:
        atmbalance += amt
        userbalance += amt
        print("Amount deposited successfully")
    else:
        print("Try again")

def update():
    global pin
    p = int(input("Enter old pin: "))
    if p == pin:
        p = int(input("Enter new pin: "))
        if len(str(p)) == 4 and p > 0:
            pin = p
            print("Pin changed successfully")
        else:
            print("Invalid pin format")
    else:
        print("Wrong pin")

def transact():
    global flag
    x = int(input("Enter your choice: \n 1. Deposit \n 2. Withdrawal \n 3. Balance enquiry \n 4. Pin Change \n 5. Exit \n"))
    match x:
        case 1:
            y = int(input("Enter amount to be deposited: "))
            deposit(y)
        case 2:
            z = int(input("Enter amount to be withdrawn: "))
            withdraw(z)
        case 3:
            print(f"Your balance is {userbalance}")
        case 4:
            update()
        case 5:
            print("Thank you")
            flag = 1
            return  # Exit the transact() function immediately after setting flag to 1
        case _:
            print("Please try again")

ch = 'y'
z = int(input("Enter pin: "))
while True:
    if z == pin:
        while ch == 'y':
            transact()
        ch = input("Continue? (y/n): ")
    else:
        print("Wrong pin")
    
    if flag == 1:
        break  # Exit the while loop if flag becomes 1
