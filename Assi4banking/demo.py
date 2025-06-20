
from banking import *

def input_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")
def main():
    print("Welcome to the Banking System!")
    owner1 = input("Enter name for Savings Account: ")
    bal1 = input_float("Enter initial balance: ")
    rate = input_float("Enter interest rate (e.g., 0.05 for 5%): ")
    savings = SavingsAccount(owner1, bal1, rate)
    owner2 = input("Enter name for Checking Account: ")
    bal2 = input_float("Enter initial balance: ")
    limit = input_float("Enter overdraft limit: ")
    checking = CheckingAccount(owner2, bal2, limit)
    print("\nApplying interest to Savings Account...")
    savings.apply_interest()
    print("Balance after interest:", savings.balance)
    amt = input_float("Enter amount to withdraw from Checking Account: ")
    try:
        checking.withdraw(amt)
        print("Withdrawal successful.")
    except ValueError as e:
        print("Error:", e)
    merged = savings + checking
    print("\nMerged Account:", merged)
    cust_name = input("Enter customer name: ")
    customer = Customer(cust_name)
    customer.add_account(savings)
    customer.add_account(checking)
    print("Total customer balance:", customer.total_balance())
    amt = input_float("Enter amount to transfer from Savings to Checking: ")
    try:
        customer.transfer(savings, checking, amt)
        print("Transfer successful.")
    except ValueError as e:
        print("Transfer failed:", e)
    for acc in customer.accounts:
        print_account_summary(acc)
    class FakeAccount:
        def __init__(self):
            self.owner = "Ghost"
            self.balance = 123.45
    print_account_summary(FakeAccount())
if __name__ == "__main__":
    main()
