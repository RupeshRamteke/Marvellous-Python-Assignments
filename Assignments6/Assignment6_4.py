def main():

    print ("Enter the number")
    num = int(input())
    
    fact = 1
    for x in range(num, 1,-1):
        fact = fact*x

    print("Factorial of ",num , " is ", fact)    

if __name__=="__main__":
    main()