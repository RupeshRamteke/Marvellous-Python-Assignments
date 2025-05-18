def addition(no1,no2):
    result = no1+no2
    return result

def main():
    print("Enter first number :")
    no1 = int(input())

    print("Enter second number :")
    no2 = int(input())

    result =addition(no1,no2)
    print("addition of number is:", result)

if __name__=="__main__":
    main()