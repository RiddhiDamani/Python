# In programming, a docstring is a string literal specified in source code that is used,
# like a comment, to document a specific segment of code.
class Account(object):
    'a bank account class'

    def set(self, value):
        'set the balance to value'
        self.balance = value

    def get(self):
        'return the current balance on the account'
        return self.balance

    def deposit(self, value):
        'updates the bank account by depositing value amount'
        self.balance += value

    def withdraw(self, value):
        'updates the bank account by withdrawing value amount'
        self.balance -= value

    def __init__(self, value=0.0):
        'the constructor'
        self.balance = value

    def __repr__(self):
        return f"Account({self.balance})"

    def __str__(self):
        return f"${self.balance:.2f}"

    # Extras - for learning purpose.
    def __gt__(self, other):
        if self.balance > other.balance:
            return True
        else:
            return False

    def __add__(self, other):
        return Account(self.balance + other.balance)


# Savings class inherits the account class properties and methods.
# str() and repr() both are used to get a string representation of object.
# using repr() function then it prints with a pair of quotes and if we
# calculate a value we get more precise value than str() function.
class Savings(Account):
    'a savings account'

    def __init__(self, amount=100.0, rate=0.001):
        'the constructor'
        Account.__init__(self, amount)
        self.rate = rate

    def setRate(self, value):
        'set the yearly interest rate'
        self.rate = value

    def addInterest(self):
        'add one month of interest to the balance'
        self.balance += self.balance * (self.rate / 12)

    def get(self):
        'prints the value of the balance'
        print(str(self))

    def __repr__(self):
        return f"Savings({self.balance}, {self.rate})"

    def __str__(self):
        return f'balance = ${self.balance:.2f}\nrate = {self.rate}%'


a1 = Account(20000)
a2 = Account(30000)
s1 = Savings(10000)

a1.deposit(1000)
a1.withdraw(4000)
a2.withdraw(10500)
a1.withdraw(3500)
print(f"a1's balance:, {a1.balance}")
print(f"a2's balance:, {a2.balance}")

x = a1.__repr__()
print(x)

# str() is used for creating output for end user while
# repr() is mainly used for debugging and development.
# repr’s goal is to be unambiguous and str’s is to be readable.
# For example, if we suspect a float has a small rounding error, repr will show us while str may not.
# repr() compute the “official” string representation of an object (a representation that has all information
# about the object)
# and str() is used to compute the “informal” string representation of an object (a representation
# that is useful for printing the object).
