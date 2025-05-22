def main():

    print(" Enter first number")
    a = int(input())

    print("Entet second number")
    b = int(input())

    print("Enter third number")
    c = int(input())


    if (a > b):
        if(a > c):
            print("Largest va;ie is:", a)
        else:
            print("Largest valiue is :", c)
    elif(b > c):
        print("Largest valiue is :", b)
    else:
        print("Largest valiue is :", c)

if __name__=="__main__":
    main()        