class BankAccount:

    ROI = 10.5

    def __init__(self,a,b):
        self.Name = a
        self.Amount = b


    def Deposit(self,Amount):
        self.Amount = self.Amount + Amount

    def Withdraw(self,Amount):    
        self.Amount = self.Amount - Amount

    def CalculateInterest(self):   
        Interest = 0
        Interest = (self.Amount * BankAccount.ROI * 1) / 100
        return Interest

    def Display(self):
        print(self.Name, self.Amount, end = " ")

def main():

    BankAcc = BankAccount("Rupesh", 10000)
    IntAmt= BankAcc.CalculateInterest()

    print("Interest amount based on amount is :",IntAmt)

if __name__=="__main__":
    main()             

    

