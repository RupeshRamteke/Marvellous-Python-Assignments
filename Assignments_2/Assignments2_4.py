def addfact(no):
    fact = 0
    for x in range(1,no):
        if(no%x== 0):
            fact = fact + x
    return fact
        
        
def main() : 
    print("Enter the pattern")
    no = int(input())  


    result = addfact(no)
    print("Factorial number is:", result)

if __name__=="__main__":
    main()