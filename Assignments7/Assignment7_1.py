sqr = lambda a : a*a
cube = lambda b : b**3

def main():
    print("Enter the number")
    num = int(input())

    res = sqr(num)
    print("Square of ",num , " is " , res)

    res = cube(num)
    print("Square of ",num , " is " , res)

if __name__=="__main__":
    main()    x