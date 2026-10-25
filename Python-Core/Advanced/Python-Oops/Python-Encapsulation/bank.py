class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder    # public
        self.__balance = balance                # private

    # Method to deposit
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ₹{amount}")
        else:
            print("Deposit amount must be positive.")

    # Method to withdraw
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ₹{amount}")
        else:
            print("Invalid withdrawal amount.")

    # Getter method (to read balance safely)
    def get_balance(self):
        return self.__balance
acc = BankAccount("John", 5000)

acc.deposit(2000)
acc.withdraw(1000)
print("Balance:", acc.get_balance())

# Trying to access private attribute directly
#print(acc.__balance)   # ❌ Error: AttributeError
