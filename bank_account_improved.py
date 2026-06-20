import random

# PARENT CLASS
class BankAccount:
    def __init__(self, name, email, address):
        # ENCAPSULATION
        self.name = name
        self.email = email
        self.address = address
        self.balance = 0
        self.account_number = random.randint(1000, 9999)
        self.transaction_history = []
        self.loan_limit = 2
        self.loan_taken = 0

    def deposit(self, amount):
        # ENCAPSULATION
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited ${amount}")
            return f"${amount} deposited successfully."
        return "Invalid deposit amount."

    def withdraw(self, amount):
        # ENCAPSULATION: Data integrity check
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")
            return f"${amount} withdrawn successfully."
        return "Withdrawal amount exceeded."

    def check_balance(self):
        return f"Available balance: ${self.balance}"

    def check_transaction_history(self):
        return self.transaction_history

    def take_loan(self, amount):
        # ABSTRACTION
        if self.loan_limit > 0:
            self.balance += amount
            self.loan_taken += amount
            self.loan_limit -= 1
            self.transaction_history.append(f"Loan taken: ${amount}")
            return f"Loan of ${amount} taken successfully."
        return "You have reached the maximum loan limit."

    def transfer(self, target_account, amount):
        # ABSTRACTION
        if self.balance >= amount:
            self.balance -= amount
            target_account.balance += amount
            self.transaction_history.append(f"Transferred ${amount} to Acct #{target_account.account_number}")
            target_account.transaction_history.append(f"Received ${amount} from Acct #{self.account_number}")
            return f"${amount} transferred successfully."
        return "Insufficient funds for transfer."


    def apply_yearly_update(self):
        # POLYMORPHISM
        pass

# INHERITANCE
class SavingsAccount(BankAccount):
    def __init__(self, name, email, address, interest_rate=0.05):
        super().__init__(name, email, address)
        self.interest_rate = interest_rate

    # POLYMORPHISM
    def apply_yearly_update(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        self.transaction_history.append(f"Yearly Interest Added: ${interest:.2f}")
        return f"Savings Update: Added ${interest:.2f} interest at {self.interest_rate*100}%"

# INHERITANCE
class CheckingAccount(BankAccount):         # INHERITANCE
    def __init__(self, name, email, address, monthly_fee=12):
        super().__init__(name, email, address)
        self.monthly_fee = monthly_fee

    # POLYMORPHISM
    def apply_yearly_update(self):
        if self.balance >= self.monthly_fee:
            self.balance -= self.monthly_fee
            self.transaction_history.append(f"Monthly Maintenance Fee Charged: ${self.monthly_fee}")
            return f"Checking Update: Charged monthly maintenance fee of ${self.monthly_fee}"
        return "Checking Update: Insufficient funds to charge maintenance fee."


