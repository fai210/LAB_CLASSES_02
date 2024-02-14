from bank import BankAccount

account1 = BankAccount("Fai", 1000)

new_balance = account1.depsot(500)
print("New balance:", new_balance)
try:
    new_balance = account1.withdraw(150)
    print("New balance:", new_balance)
except Exception as e:
    print("Error:", str(e))

try:
    new_balance = account1.withdraw(1200)
    print("New balance:", new_balance)
except Exception as e:
    print("Error:", str(e))
    
current_balance = account1.get_inital_balance()
print("Current balance:", current_balance)