import Arithematic

def main():

    print("Enter first number")
    value1 = int(input())

    print("Enter second number")
    value2 = int(input())

    result = Arithematic.add(value1,value2)
    print("Addition is ", result)

    result = Arithematic.Sub(value1,value2)
    print("Substraction  is ", result)

    result = Arithematic.Mul(value1,value2)
    print("Multiplication is ", result)

    result = Arithematic.Div(value1,value2)
    print("Division  is ", result)


if __name__=="__main__":
    main()

