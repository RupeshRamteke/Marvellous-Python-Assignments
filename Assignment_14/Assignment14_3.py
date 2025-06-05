class Book:

    def __init__(self,):
        self._price = 0

    def set(self,price):
        self._price = price

    def get(self):
        return self._price
    
def main():

    Obj = Book()

    Obj.set(100)

    price = Obj.get()
    print("Price of book is :",price)

if __name__=="__main__":
    main()
        


