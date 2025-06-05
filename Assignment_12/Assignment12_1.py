class demo:
    value = "class variable"

    def __init__(self,a,b):
        self.no1 = a
        self.no2 = b

    def fun(self):
        print("The value of No1 varaibel is :",self.no1)

    def gun(self):
        print("The value of No2 variable is :",self.no2)

def main():

    Obj1 = demo(11,21) 
    Obj2 = demo(51,101)

    Obj1.fun()
    Obj2.fun()

    Obj1.gun()
    Obj2.gun()

if __name__=="__main__":
    main()
    




        