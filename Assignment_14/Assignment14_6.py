class calculator:

    def __init__(self,a,b):
        self.value1 = a
        self.value2 = b

    def Add(self):
        res = 0
        res = self.value1 + self.value2
        return res

    def Sub(self):
        res = 0
        res = self.value1 - self.value2
        return res
    
    def Mul(self):
        res = 0
        res = self.value1 * self.value2
        return res
    
    def Div(self):
        res = 0
        res = self.value1 / self.value2
        return res
    
def main():

    print("Enter the first number :")
    a = int(input())

    print("Enter teh second number")
    b = int(input())

    obj1 = calculator(a,b)

    Total = obj1.Add()
    print("Addition of number is :",Total)
    
    Total = obj1.Sub()
    print("substraction of number is :",Total)

    Total = obj1.Mul()
    print("Multiplication of number is :",Total)

    Total = obj1.Div()
    print("Division of number is :",Total)

if __name__=="__main__":
    main()    



