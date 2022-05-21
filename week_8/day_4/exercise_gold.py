# Bank account

class BankAccount:
    def __init__(self, balance, username, password, authenticated=False):
        self.balance = balance
        self.username = username
        self.password = password
        self.authenticated = authenticated

    def authenticate(self, username, password):

        if self.username == username and self.password == password:
            self.authenticated = True
        return self.authenticated

    def deposit(self):
        if not self.authenticated:
            raise Exception("You are not authenticated...")
        else:
            input_deposit = int(input("What is your deposit amount: "))
            if input_deposit <= 0:
                raise Exception("Amount is not correct")
            self.balance += input_deposit
            return self.balance

    def withdraw(self):
        user = input("enter username: ")
        psswd = input("Enter your password")
        self.authenticate(username=user, password=psswd)
        if not self.authenticated:
            raise Exception("You are not authenticated...")
        else:
            withdrawal = int(input("How much do you want to withdraw: "))
            if withdrawal <= 0 or withdrawal > self.balance:
                raise Exception("Insufficient balance or incorrect input")
            self.balance -= withdrawal
            return self.balance


class MinimumBalanceAccount(BankAccount):
    def __init__(self, balance, username, password, authenticated=False, minimum_balance=0):
        super().__init__(balance, username, password, authenticated=False)
        self.minimum_balance = minimum_balance
        print(self.minimum_balance, self.balance)

    def withdraw(self):
        if self.balance < self.minimum_balance:
            raise Exception("You can't withdraw this amount.")
        else:
            withdrawal = int(input("How much do you want to withdraw: "))
            if withdrawal <= 0 or withdrawal > self.balance:
                raise Exception("Insufficient balance or incorrect input")
            self.balance -= withdrawal
        return self.balance


class ATM:
    def __init__(self, account_list, try_limit):
        self.account_list = account_list
        try:
            self.try_limit = try_limit
            if int(self.try_limit) <= 0 or isinstance(self.try_limit, int) is False:
                raise ValueError("That is not a positive number!")
        except ValueError as ve:
            self.try_limit = 2
        result = isinstance(self.account_list, BankAccount)
        self.current_tries = 0
        self.show_main_menu()
        print(self.account_list)
        print(result)

    def show_main_menu(self):

        print("\nMenu:\n1- Log in\n2- Exit")
        user_input = input("Make a choice: ")
        if user_input == '1':
            self.log_in()
        elif user_input == '2':
            pass
        else:
            print("Wrong input")

    def log_in(self):
        username_input = input("Enter username: ")
        password_input = input("Enter password: ")
        # BankAccount.authenticate(username=username_input, password=password_input)
        # if not BankAccount.authenticated:
        #     raise Exception("You are not authenticated...")
        # else:
        #     print("Logged in")


my_account1 = BankAccount(23, "user1", "password1")
my_account2 = BankAccount(23, "user2", "password2")
my_account3 = BankAccount(23, "user3", "password3")
my_account4 = MinimumBalanceAccount(balance=34, minimum_balance=45, username='user4', password='password4')
my_account5 = 5
# ba = MinimumBalanceAccount(56)
# my_account.authenticate("username", "password")
list_accounts = [my_account1, my_account2, my_account3]

my_atm = ATM(list_accounts, 3)
print(my_atm.try_limit)

# my_account.deposit()
# my_account.withdraw()
print(my_account1.balance)
# ba.withdraw()
# print(ba.balance)
