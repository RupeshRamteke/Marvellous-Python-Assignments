class Rectangle:

    def __init__(self,a,b,):
        self.length = a
        self.width = b

    def Area(self):
        area = 0
        area = self.length * self.width
        return area
    
    def Perimeter(self):
        perimeter = 0
        perimeter = 2 * (self.length + self.width)
        return perimeter
    
def main():

    Obj = Rectangle(10,5)

    Area = Obj.Area()
    print("Area of Rectangle:",Area)

    Perimeter = Obj.Perimeter()

    print("Perimter of Rectangle:", Perimeter)


if __name__=="__main__":
    main()


    

        

