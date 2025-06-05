class Circle:
    PI = 3.14

    def __init__(self):
        self.radius = 0.0
        self.area = 0.0
        self.circumference = 0.0

    def Accept(self,r):
        self.radius  = r

    def calculatearea(self):
        self.area = 0
        self.area = Circle.PI * self.radius * self.radius
    
    def calculatecircumference(self):
        self.circumference = 0
        self.circumference = 2 * Circle.PI * self.radius

    def Display(self):
        print("Radius of Circle is :",self.radius)
        print("Area of Circel is :",self.area)
        print("Area of Circumference is : ",self.circumference)


def main():

    print("Enter radius of Circle :")
    a = int(input())

    Cir = Circle()
    Cir.Accept(a)
    Cir.calculatearea()
    Cir.calculatecircumference()
    Cir.Display()

    print("Enter radius of Circle :")
    b = int(input())

    Cir = Circle()
    Cir.Accept(b)
    Cir.calculatearea()
    Cir.calculatecircumference()
    Cir.Display()

if __name__=="__main__":
    main()
