from bank_account_improved import SavingsAccount, CheckingAccount

class Admin:
    def __init__(self):
        self.user_accounts = []

    def create_account(self, name, email, address, account_type):
        if account_type.lower() == "savings":
            account = SavingsAccount(name, email, address)
        else:
            account = CheckingAccount(name, email, address)
        self.user_accounts.append(account)
        return account

    def delete_account(self, account):
        if account in self.user_accounts:
            self.user_accounts.remove(account)
            return "Account deleted successfully."
        else:
            return "Account not found."

    def list_accounts(self):
        return [f"{type(acc).__name__} belonging to {acc.name} (Acct #{acc.account_number})" for acc in self.user_accounts]

    def total_balance(self):
        total_balance = sum(account.balance for account in self.user_accounts)
        return f"Total balance : ${total_balance}"

    def total_loan_amount(self):
        total_loan = sum(account.loan_taken for account in self.user_accounts)
        return f"Total loan amount : ${total_loan}"

    def toggle_loan_feature(self, enable=True):
        for account in self.user_accounts:
            account.loan_limit = 2 if enable else 0
        return "Loan feature enabled" if enable else "Loan feature disabled"
