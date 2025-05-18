def factorial(no):
    fact = 1
    for x in range(no,0,-1):
        fact = fact * x
    return fact
        
        
def main() : 
    print("Enter the pattern")
    no = int(input())  


    result = factorial(no)
    print("Factorial number is:", result)

if __name__=="__main__":
    main()