class BankAccount:

    balance = 0

    def add_balance(self, amount):
        self.balance += amount
        print(f"Added {amount} to the account. Current balance: {self.balance}")


    def subtract_balance(self, amount):
        self.balance -= amount
        print(f"Subtracted {amount} to the account. Current balance {self.balance}")


class SavingsAccount(BankAccount):
    
    def __init__(self, balance, min_balance):
        self.balance = balance
        self.min_balance = min_balance

    def subtract_balance(self, amount):
        if self.balance - amount < self.min_balance:
            raise ValueError(f"Cannot substract {amount} from the account. Minimum balance of {self.min_balance} must be maintained")
        else:
            super().subtract_balance(amount)
            print(f"Subtracting {amount} from the account. Current balance: {self.balance}")


bank_account = BankAccount()
bank_account.add_balance(1000)
bank_account.subtract_balance(500)
saving_account = SavingsAccount(200, 100)
saving_account.subtract_balance(50)