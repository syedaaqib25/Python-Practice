
class BankAccount:
    total_accounts = 0
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.__balance = balance
        BankAccount.total_accounts += 1
    def deposit(self, amt: float):
        if amt <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.__balance += amt
    def withdraw(self, amt: float):
        if amt <= 0 or amt > self.__balance:
            raise ValueError("Invalid withdrawal amount.")
        self.__balance -= amt
    @property
    def balance(self) -> float:
        return self.__balance
    @balance.setter
    def balance(self, value: float):
        if value < 0:
            raise ValueError("Balance cannot be negative.")
        self.__balance = value
    def __str__(self):
        return f"BankAccount(owner='{self.owner}', balance={self.balance:.2f})"
    def __repr__(self):
        return f"<BankAccount owner={self.owner} balance={self.balance:.2f}>"
    def __add__(self, other):
        if not isinstance(other, BankAccount):
            return NotImplemented
        new_owner = f"{self.owner} & {other.owner}"
        new_balance = self.balance + other.balance
        return BankAccount(new_owner, new_balance)
class SavingsAccount(BankAccount):
    def __init__(self, owner: str, balance: float = 0.0, interest_rate: float = 0.01):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
    def apply_interest(self):
        self.deposit(self.balance * self.interest_rate)
class CheckingAccount(BankAccount):
    def __init__(self, owner: str, balance: float = 0.0, overdraft_limit: float = 100.0):
        super().__init__(owner, balance)
        self._overdraft_limit = overdraft_limit
    def withdraw(self, amt: float):
        if amt < 0 or amt > (self.balance + self._overdraft_limit):
            raise ValueError("Overdraft limit exceeded.")
        self._BankAccount__balance -= amt
    @property
    def overdraft_limit(self):
        return self._overdraft_limit
    @overdraft_limit.setter
    def overdraft_limit(self, value: float):
        if value < 0:
            raise ValueError("Overdraft limit must be non-negative.")
        self._overdraft_limit = value
class Customer:
    def __init__(self, name: str):
        self.name = name
        self.accounts = []
    def add_account(self, account: BankAccount):
        self.accounts.append(account)
    def total_balance(self):
        return sum(account.balance for account in self.accounts)
    def transfer(self, from_acc: BankAccount, to_acc: BankAccount, amt: float):
        from_acc.withdraw(amt)
        to_acc.deposit(amt)
def print_account_summary(obj):
    try:
        print(f"{obj.owner} has balance {obj.balance}")
    except AttributeError:
        print("Invalid account object")
