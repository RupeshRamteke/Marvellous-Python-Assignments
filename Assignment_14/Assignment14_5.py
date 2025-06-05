class BankAccount:

    def __init__(self,a,b,c):
        self.AccountNum = a
        self.name = b
        self.balance = c

    def deposit(self,amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self,amount):
        self.balance = self.balance - amount
        return self.balance

    def Display(self):
        print("Display Account number ;",self.AccountNum)
        print("Display name of Account holder :",self.name)
        print("Dispaly balance in account :",self.balance)

def main():

    Obj = BankAccount( 1010105, "Rupesh", 1000)
    
    print("Initiall balance")
    Obj.Display()

    Obj.deposit(2500)
    print("Balance after deposit :")
    Obj.Display()

    Obj.withdraw(1000)
    print("Balance after Withdrawal:")
    Obj.Display()

if __name__=="__main__" :
    main()   



