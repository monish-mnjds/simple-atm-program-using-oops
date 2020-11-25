class BankAccount():
    def __init__(self):
        self.balance = 0
    def deposit(self,amount):
        self.balance += amount
    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('\nEntered amount is',amount,'& Your balance is',self.balance)
    def statement(self):
        return self.balance
a = BankAccount()
while 1:
    option = input('\nOption: ')
    if option == '1':
        dep = int(input('\nDepositing amount: '))
        a.deposit(dep)
    elif option == '2':
        wit = int(input('\nWithdrawing amount: '))
        a.withdraw(wit)
    elif option == '3':
        print('\nYour A/c balance is',a.statement())
    else:
        print('\nValid options are 1, 2, 3.....')
    cont = input('\nY / N ? -> ')
    if cont == 'Y' or cont == 'y':
        continue
    else:
        break