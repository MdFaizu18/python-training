import accounts, transactions

accounts.create_account("Faizu", 1000)
transactions.deposit("Faizu", 500)
transactions.withdraw("Faizu", 200)
print("Balance:", accounts.show_balance("Faizu"))
