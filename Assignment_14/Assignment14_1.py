class employee:

    def __init__(self,a,b,c):
        self.name = a
        self.emp_id = b
        self.salary = c

    def display(self):
        print("Name :",self.name)
        print("Employee ID :",self.emp_id)
        print("Salary :",self.salary)

def main():

        obj = employee("Rohit",101,5000)
        obj.display()

if __name__=="__main__":
    main()    


