def main():

    print ("Enter the number")
    num = int(input())
    
    ans = "It is prime number"
    i = 2
    while (i < num):
        if(num % i == 0):
            ans = "It is not prime number"
            break
        i = i+1

    print (ans)    

if __name__=="__main__":
    main()