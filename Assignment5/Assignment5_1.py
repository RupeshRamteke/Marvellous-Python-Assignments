def sum(no1,no2):
    ans = 0
    ans = no1+no2
    print("Addition is :", ans)

def diff(no1,no2):
    ans = 0
    if(no2>no1):
        ans = no2-no1
    else:
        ans = no1-no2

    print("Substraction is :", ans)

def product(no1,no2):
    if(no1 == 0 or no2 == 0):
        print ("Both number should be greater than 0")
    else:
        mul=0
        mul= no1*no2
        print("Product is :", mul)

def division(no1,no2):
    if(no1 == 0 or no2 == 0):
        print ("Both number should be greater than 0")
    elif(no2 > 0):
        div = no1/no2
        print("Division is :", div)
    elif(no1 > 0):
        div=no2/no1
        print("Divsion is :",div)

def main():
    print("Enter first number")
    val1 = int(input())
    
    print("Enter second number")
    val2=int(input())

    sum(val1,val2)
    diff(val1,val2)
    product(val1,val2)
    division(val1,val2)  

if __name__=="__main__":
    main()



