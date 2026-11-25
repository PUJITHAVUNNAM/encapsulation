class BankAccount:
    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print("Withdrawn:", amount)

    def show_balance(self):
        print("Balance:", self.__balance)


b = BankAccount(12345, 5000)

b.deposit(1000)
b.withdraw(2000)
b.show_balance()

b.__balance = 10000
b.show_balance()