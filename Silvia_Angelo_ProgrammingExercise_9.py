#Create a BankAcct Class that contains at least the following state information:
# name, account number, amount and interest rate. In addition to an __init__ method,
# the class should support methods for adjusting the interest rate, for withdrawing
# and depositing, and for giving a balance. You should also include a method to
# calculate the interest based on the number of days. Use the __str__ method to
# display balances and interest amounts.
# Create a test function to test the different methods in the BankAcct Class.
class BankAcct:
    def __init__(self, name, acct_num, amount, int_rate):
        self.name = name
        self.acct_num = acct_num
        self.amount = amount
        self.int_rate = int_rate

    def deposit(self, deposit_amount):
        self.amount += deposit_amount

    def withdrawal (self, with_amount):
        self.amount -= with_amount

    def adjust_interest_rate(self, new_rate):
        self.int_rate = new_rate

    def get_balance(self):
        return self.amount

    def calc_interest(self, num_of_days):
        interest = self.amount * (self.int_rate / 365) * num_of_days
        return interest

    def __str__(self):
        interest_snapshot = self.calc_interest(30)
        # Fixed the indentation and removed 'self.' from interest_snapshot below
        return (f"Account Holder: {self.name}\n"
                f"Account Number: {self.acct_num}\n"
                f"Current Balance: ${self.amount:,.2f}\n"
                f"Estimated Interest: ${interest_snapshot:,.2f}")

# --- Test Function --
def test_bank_acct():
    print("--- Starting Bank Account Test ---")
    #Initialize account
    account = BankAcct("John Doe", "123456", 1000.00, .05)
    print(account)
    print("-" * 30)

    #Test Deposit
    account.deposit(5000.00)
    print(f"Deposit successful! New balance: ${account.amount:,.2f}")

    #Test Withdrawl
    account.withdrawal(1500.00)
    print(f"Withdrawal successful! New balance: ${account.amount:,.2f}")
    print("-" * 30)

    #Test Interest Rate Adjustment & Calculation
    account.adjust_interest_rate(0.06)
    print(f"Interest rate adjusted to: {account.int_rate * 100}%")

    interest_earned = account.calc_interest(365)
    print(f"Interest earned over 365 days: ${interest_earned:.2f}")
    print("-" * 30)

    #Final amount
    print ("Final Account Amount: ")
    print(account)

if __name__ == "__main__":
    test_bank_acct()