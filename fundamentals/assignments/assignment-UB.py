class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.all_account = []
    def create_account(self,int_rate,balance,account_no):
        account=BankAccount(int_rate, balance=0, account_no=00000)	
        # added this line my_account["account_no"]= account.account_no
        my_account = {}
        my_account["acc_obj"]=account  
        self.all_account.append(my_account)
        print(self.all_account)
        for i in range(len(self.all_account)):
            for value in self.all_account[i].values():
                print(value)
"""     def example_method(self):
        self.account.deposit(100)		# we can call the BankAccount instance's methods
        print(self.account.balance)		# or access its attributes
        return self """
class BankAccount:
    # don't forget to add some default values for these parameters!
	# your code here! (remember, this is where we specify the attributes for our class)
    # don't worry about user info here; we'll involve the User class soon 
    def __init__(self, int_rate=0, balance=0,account_no=00000):
        self.int_rate = int_rate
        self.balance = balance
        self.account_no = account_no
    """
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
    """
Bob = User("BObmarley","Bob@marley.com")
Bob.create_account(1,200,4000000)