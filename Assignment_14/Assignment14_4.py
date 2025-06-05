class Student:
    school_name = "XYZ"

    def __init__(self,a,b):
        self.name = a
        self.roll = b

    def Display(self):
        print("Name of the student :",self.name)
        print("Roll number of student :", self.roll)
        print("Name of the school :",Student.school_name)

def main():

    obj = Student("Rupesh", 11)

    print("Initially")
    obj.Display()

    Student.school_name = "ACEM"
    
    print("After class name change")
    obj.Display()

if __name__=="__main__":
    main()    




