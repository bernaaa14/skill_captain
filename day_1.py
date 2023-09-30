class BankAccount:
    #Constructor that initializes account_number, account_holder_name, account_balance
    def __init__(self,account_number, account_holder_name, account_balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.account_balance = account_balance

    # Function that tracks the money deposits
    def deposit_money(self, deposit_amount):
        self.account_balance=self.account_balance+deposit_amount

    # Function that tracks the money withdrawal
    def withdraw_money(self, withdraw_amount):
        # if statement to decline transaction when withdraw amount is greater than account balance
        if self.account_balance<withdraw_amount:
            print("Sorry not enough balance")
        else:
            self.account_balance= self.account_balance - withdraw_amount

    #Function to display updated account information
    def display_information(self):
        print()
        print("--------ACCOUNT INFORMATION--------")
        print("Account number: " , self.account_number)
        print("Account Holder name ", self.account_holder_name)
        print("Account Balance: ", self.account_balance)

account = BankAccount("1234", "Badr", 1000)
account.display_information()  # Display initial account info

account.withdraw_money(100) # Withdraw 100
account.display_information() # Display updated info

account.deposit_money(100)  # Deposit 600
account.display_information()  # Display updated account info

account.withdraw_money(1100)  # Withdraw 1100
account.display_information()  # Display updated account info ( Decline transaction)


