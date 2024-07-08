# Bank Account-> Saving Account -> Checking Account 
# depositing -> withdrawing -> checking the balance 
# account Transaction track -> calculate interest for saving account -> encapsulation, inheritance

class Bank_Account:

    def __init__(self,uname,passw,balance=0) -> None: #creating a new account in bank
        self.__uname=uname
        self.__passw=passw
        self.balance=balance
        self.transaction=[]
        
    @property
    def uname(self):
        return self.__uname
    
    @uname.setter
    def uname(self,value): #change username function
        self.__uname=value

    @property
    def passw(self):
        return self.passw
    
    @passw.setter
    def passw(self,value): #change password function
        self.__passw=value 

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            self.add_transaction(f"Deposited: ${amount}")
        else:
            raise ValueError("Deposit amount must be positive")

    def withdraw(self,amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                self.add_transaction(f"Withdrew: ${amount}")
            else:
                raise ValueError("Insufficient funds")
        else:
            raise ValueError("Withdrawal amount must be positive")

    def chechBalance(self):
        return self.balance
    
    def add_transaction(self,to):
        self.transaction.append(to)

    def __str__(self) -> str:
        return f"Username {self.__uname} , Balance:{self.balance} , Transaction: {self.transaction}"
    
class SavingsAccount(Bank_Account):
    def __init__(self, account_number, initial_balance=0, interest_rate=0.01):
        super().__init__(account_number, initial_balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        self.add_transaction(f"Interest: ${interest}")

    def __str__(self):
        return f"Savings Account - {super().__str__()}, Interest Rate: {self.interest_rate * 100}%"
    
class CheckingAccount(Bank_Account):
    def __init__(self, account_number, initial_balance=0, overdraft_limit=0):
        super().__init__(account_number, initial_balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > 0:
            if self.balance + self.overdraft_limit >= amount:
                self.balance -= amount
                self.add_transaction(f"Withdrew: ${amount}")
            else:
                raise ValueError("Insufficient funds and overdraft limit exceeded")
        else:
            raise ValueError("Withdrawal amount must be positive")

    def __str__(self):
        return f"Checking Account - {super().__str__()}, Overdraft Limit: ${self.overdraft_limit}"

# Create a SavingsAccount
savings = SavingsAccount("S001", initial_balance=1000, interest_rate=0.05)
print(savings)
savings.deposit(500)
savings.withdraw(200)
savings.calculate_interest()
print(savings)
print("Transactions:", savings.transaction)
print()
# Create a CheckingAccount
checking = CheckingAccount("C001", initial_balance=500, overdraft_limit=200)
print(checking)
checking.deposit(300)
# checking.withdraw(600)
checking.withdraw(200)  # This should raise an error due to insufficient funds and overdraft limit
print(checking)
print("Transactions:", checking.transaction)



        
    
    
    