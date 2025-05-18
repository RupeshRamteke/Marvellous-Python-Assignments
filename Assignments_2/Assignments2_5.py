def prime(no):
    ans = "It is prime number"
    i = 2
    while (i < no): 
        if(no % i == 0) :
            ans = "It is not prime number"
            break
        i = i + 1
    return ans

def main() : 
    print("Enter the number")
    no = int(input())  

    result = prime(no)
    print(result)

if __name__=="__main__":
    main()