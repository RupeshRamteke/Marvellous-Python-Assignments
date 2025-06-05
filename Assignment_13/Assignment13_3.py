class number:
    def __init__(self,a):
        self.value = a

    def chkPrime(self):

        ans =True
        i = 2
        while (i < self.value) :
            if(self.value % i == 0):
                ans = False
                break
            i = i + 1
        if(ans == True):
            return "Prime number"
        else:
            return "Not prime number"
        
    def checkPerfect(self):
        sum = self.sumfactor()
        if(sum == self.value):
            return "Perfect number"
        else:
            return "Not perfect number"
        
    def sumfactor(self):
        sum = 0
        i=1
        while (i < self.value):
            if(self.value % i == 0):
                sum = sum + 1
            i = i + 1
        return sum
    
    def factor(self):
        factorslist = []
        i = 1
        while(i < self.value):
            if(self.value % i == 0):
                factorslist.append(i)
            i = i+1
        return factorslist
    
def main():

    print("Enter the number")
    a = int(input())

    obj1 = number(a)
    ret = obj1.chkPrime()
    print(a,"is", ret, end = " ")
    print("\n")

    ret = obj1.checkPerfect()
    print(a,"is", ret, end =" ")
    print("\n")

    ret = obj1.sumfactor()
    print("sum of factor is : ",ret, end = " ")

    ret = obj1.factor()
    print("Factor list is :", ret , end =" ")
    print("\n")

if __name__=="__main__":
    main()
        
        