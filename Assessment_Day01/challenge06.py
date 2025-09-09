# Challenge 6: Bank Account Simulation

balance = 1000

def deposit(amount):
    global balance
    balance += amount
    print(f"Deposit {amount} → Balance: {balance}")

def withdraw(amount):
    global balance
    if balance >= amount:
        balance -= amount
        print(f"Withdraw {amount} → Balance: {balance}")
    else:
        print(f"Withdraw {amount} → Insufficient funds! Balance: {balance}")

deposit(200)
withdraw(500)
withdraw(1000)