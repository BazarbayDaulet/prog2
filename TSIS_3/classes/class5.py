class Bank():
    def __init__ (self, money, name):
        self.money = money
        self.name= name
        
    def owner(self):
        self.name = input("Введите имя")
        
    def balance(self):
        print(self.money)
        
    def deposit(self):
        plus = int(input("введите сумму: "))
        self.money+=plus
        
    def withdraw (self):
        minus = int(input("Введите сумму"))
        if self.money<minus:
            print("У вас недостаточно средств")
        else:
            self.money-=minus
            
m = 0
names = "unknown"
Baz = Bank(m, names)
Baz.owner()
while 1:
    a = int(input("Введите число: 1.balance 2.deposit 3.withdraw: "))
    if a == 1:
        Baz.balance()
    if a == 2:
        Baz.deposit()
    if a == 3:
        Baz.withdraw()
        
        