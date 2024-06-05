#python banking program

def show_balance():
    print(f"Your balance is ${balance: .2f}")


def deposit():
    amount = float(input("Enter an amount to be deposited: "))

    if amount < 0:
        print("That's not a valid amount")
    else:
        return 


def withdraw():
    pass

balance = 100
is_running  = True

while is_running:
    print("Banking Program")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice: ")
    print("-----------------")
    if choice == "1":
        show_balance()
    elif choice == "2":
        balance += deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        is_running == False
    else:
        print("Not Valid")
    
    print("-----------------")

