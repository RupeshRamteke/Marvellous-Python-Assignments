class product:

    def __init__(self,name,price):
        self.name = name
        self.price = price

    def __eq__(self,b):
        if(self.price == b.price):
            print(self.name,"and", b.name,"price are same", end=" ")
        else:
            print(self.name,"and",b.name,"price are not same", end=" ")
        print("\n")

def main():

    product1 = product("Laptop",45000)
    product2 = product("mouse",5000)

    product1.__eq__(product2)

    product1 = product("LED",50000)
    product2 = product("Mobile",50000)

    product1.__eq__(product2)

if __name__=="__main__":
    main()    



