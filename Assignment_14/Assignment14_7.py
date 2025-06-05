
class person:     
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Teacher(person):
    def __init__(self,name,age,sub,sal):
        self.subject = sub
        self.salary = sal
        super().__init__(name,age)


    def display(self):
        print("Name of person :",self.name)
        print("Age of person :",self.age)
        print("Name of person :",self.subject)
        print("Age of person :",self.salary)

class main():

    Obj1 = Teacher("Rupesh",40,"Mathematics",100000) 

    Obj1.display()

if __name__=="__main__":
    main()
