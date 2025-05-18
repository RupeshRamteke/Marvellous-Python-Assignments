Mul = lambda a,b : a*b

def main():
    print ("Enter first value:")
    no1 = int(input())
    
    print ("Enter second value:")
    no2 = int(input())

    result = Mul(no1,no2)

    print("Power of number is", result)

if __name__=="__main__":
        main()