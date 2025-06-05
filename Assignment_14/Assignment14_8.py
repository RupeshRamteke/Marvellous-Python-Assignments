class Vehicle:
    
    def start(self):
        print("In base class method")

class car(Vehicle):

    def start(self):
        print("In derive class method")

def main():

    Obj = car()

    Obj.start()

if __name__=="__main__":
    main()    


