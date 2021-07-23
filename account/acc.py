class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = float(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount
        self.commit()

    def deposit(self, amount):
        self.balance = self.balance + amount
        self.commit()

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))


class Checking(Account):
    def __init__(self, filepath):
        Account.__init__(self, filepath)

    def transfer(self, amount):
        fee = 1 * amount / 100
        self.balance = self.balance - amount - fee
        self.commit()


checking = Checking("./balance.txt")
checking.transfer(100)
print(checking.balance)
