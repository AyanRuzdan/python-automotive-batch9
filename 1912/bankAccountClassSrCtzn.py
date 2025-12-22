class BankAccount:
    # Class-level set to track all account numbers and prevent duplicates
    accounts = set()

    def __init__(self, account_number, customer_name, age, initial_balance=0.0):
        try:
            # Check if account number already exists
            if account_number in BankAccount.accounts:
                raise ValueError(
                    f"Account number {account_number} already exists")

            # Validate initial balance is non-negative
            if initial_balance < 0:
                raise ValueError("Initial balance cannot be negative")

            # Store account details
            self.account_number = account_number
            self.customer_name = customer_name
            self.age = age
            self.balance = initial_balance

            # Add account number to class-level set to track it globally
            BankAccount.accounts.add(account_number)

        except ValueError as e:
            print("Account creation failed:", e)
            raise

    def deposit(self, amount):
        try:
            # Ensure deposit amount is positive
            if amount <= 0:
                raise ValueError("Deposit amount must be positive")
            self.balance += amount
            print("%d deposited successfully" % amount)
        except ValueError as e:
            print("Deposit error:", e)

    def withdraw(self, amount):
        try:
            # Ensure withdrawal amount is positive
            if amount <= 0:
                raise ValueError("Withdrawal amount must be positive")
            # Check if sufficient balance exists
            if amount > self.balance:
                raise ValueError("Insufficient balance")
            self.balance -= amount
            print("%d withdrawn successfully" % amount)
        except ValueError as e:
            print("Withdrawal error:", e)

    def calculate_compound_interest(self, tenure):
        try:
            # Senior citizen benefit: only those 60+ can get compound interest
            if self.age < 60:
                raise ValueError(
                    "Compound interest available for senior citizens only")
            # Tenure must be positive number of years
            if tenure <= 0:
                raise ValueError("Tenure must be positive")

            # Fixed interest rate of 8% per annum
            rate = 8
            # Compound interest formula
            ci = self.balance * (1 + rate / 100) ** tenure
            ci = round(ci, 2)

        except ValueError as e:
            print("Interest calculation error:", e)
            ci = None
        return ci

    def display_details(self):
        print("-----ACCOUNT DETAILS------")
        print("A/C No.:", self.account_number)
        print("Name:", self.customer_name)
        print("Current balance:", self.balance)
        print("Age:", self.age)


# Test case 1: Senior citizen account (age 65)
acc1 = BankAccount("1001", "Michael", 65, 1000)
acc1.display_details()
acc1.deposit(500)
acc1.deposit(-200)  # Invalid: negative deposit
acc1.withdraw(200)
acc1.display_details()
print("COMPOUND INTEREST: ", acc1.calculate_compound_interest(5))
print("COMPOUND INTEREST: ", acc1.calculate_compound_interest(15))

# Test case 2: Non-senior citizen account (age 30)
acc2 = BankAccount("1002", "Ruzdan", 30)
acc2.deposit(300)
acc2.display_details()
acc2.withdraw(100000)  # Invalid: insufficient balance
acc2.withdraw(14)
print("CI: ", acc2.calculate_compound_interest(15))  # Invalid: age < 60

# Test case 3: Attempt to create duplicate account (should raise error)
try:
    acc3 = BankAccount("1001", "Ankita", 40, 1500)
except ValueError:
    pass
