class Arithmetic:

    def __init__(self):
        self.value1 = 0
        self.value2 = 0

    def Accept(self,a,b):
        self.value1 = a
        self.value2 = b

    def Addition(self):
        result = 0
        result = self.value1 + self.value2
        return result

    def Substraction(self): 
        result = 0
        result = self.value1 - self.value2
        return result   
    
    def Multiiplication(self):
        result = 0
        result = self.value1 * self.value2
        return result
    
    def Division(self):
        result = 0
        result = self.value1 / self.value2
        return result
    
def main():

    print("Enter the first number:")
    a = int(input())

    print("Enter the second number :")
    b = int(input())

    Calculate = Arithmetic()
    Calculate.Accept(a,b)

    sum = Calculate.Addition()
    print("Addition is :",sum)

    sum = Calculate.Substraction()
    print("Substraction is :",sum)

    sum = Calculate.Multiiplication()
    print("Multiplication is :",sum)

    sum = Calculate.Division()
    print("Division is :",sum)

if __name__=="__main__":
    main()



