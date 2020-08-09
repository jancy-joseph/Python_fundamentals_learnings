class User:
    def __init__(self, username, email_address):# now our method has 2 parameters!
        self.name = username			# and we use the values passed in to set the name attribute
        self.email = email_address		# and the email attribute
        self.account_balance = 0		# the account balance is set to $0, so no need for a third parameter
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received
    def make_withdrawal(self, amount):
        self.account_balance-=amount
    def display_user_balance(self):
        print("User:"+self.name+" Balance: $"+str(self.account_balance))
    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)




guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
bob = User("Another bob", "bob@bobby.com")

guido.make_deposit(100)
guido.make_deposit(200)
guido.make_deposit(300)
guido.make_withdrawal(30)

guido.display_user_balance()

monty.make_deposit(50)
monty.make_deposit(150)
monty.make_withdrawal(15)

monty.display_user_balance()

bob.make_deposit(150)
bob.make_withdrawal(15)
bob.make_withdrawal(15)
bob.make_withdrawal(15)

bob.display_user_balance()

bob.transfer_money(monty,15)

monty.display_user_balance()
bob.display_user_balance()