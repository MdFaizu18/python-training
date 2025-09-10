import accounts as acc

def deposit(name, amount):
    acc.accounts[name] += amount

def withdraw(name, amount):
    if acc.accounts[name] >= amount:
        acc.accounts[name] -= amount
    else:
        print("Insufficient balance")
