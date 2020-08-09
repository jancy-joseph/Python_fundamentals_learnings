class User:
    def __init__(self, username, email_address):# now our method has 2 parameters!
        self.name = username			# and we use the values passed in to set the name attribute
        self.email = email_address		# and the email attribute
        self.account_balance = 0
        # return self	--not correct it needs to return none --will error out 	TypeError: __init__() should return None
    # the account balance is set to $0, so no need for a third parameter 
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received
        return self
    def make_withdrawal(self, amount):
        self.account_balance-=amount
        return self
    def display_user_balance(self):
        print("User:"+self.name+" Balance: $"+str(self.account_balance))
        return self
    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self




guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
bob = User("Another bob", "bob@bobby.com")

guido.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(30).display_user_balance()

monty.make_deposit(50).make_deposit(150).make_withdrawal(15).display_user_balance()

bob.make_deposit(150).make_withdrawal(15).make_withdrawal(15).make_withdrawal(15).display_user_balance().transfer_money(monty,15)

monty.display_user_balance()
bob.display_user_balance()