class Employee:

    def __init__(self,name,salary,dept):
        self.Name = name
        self.__salary = salary
        self._dept = dept

    def display(self):
        print("Name", self.Name)
        print("Salary",self.__salary)
        print("Department :",self._dept)

def main():

    Obj = Employee("Rupesh",50000,"CBI")
    Obj.display()

if __name__=="__main__":
    main()            
        