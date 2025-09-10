accounts = {}

def create_account(name, balance=0):
    accounts[name] = balance

def show_balance(name):
    return accounts.get(name, "Account not found")
