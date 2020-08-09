class BankAccount:
    # don't forget to add some default values for these parameters!
	# your code here! (remember, this is where we specify the attributes for our class)
    # don't worry about user info here; we'll involve the User class soon 
    def __init__(self, int_rate=0, balance=0):
        self.int_rate = float(int_rate/100)
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdrawal(self, amount):
        if self.balance - amount > 0:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    def display_account_info(self):
        print("Balance :$"+str(self.balance))
        return self
    def yield_interest(self):
        self.balance+=float(self.balance*self.int_rate)
        return self
bob = BankAccount(1,1)
marley =BankAccount(1,1)
bob.deposit(1).deposit(1).deposit(1).withdrawal(6).yield_interest().display_account_info()
marley.deposit(10).deposit(10).withdrawal(1).withdrawal(1).withdrawal(6).withdrawal(1).yield_interest().display_account_info()