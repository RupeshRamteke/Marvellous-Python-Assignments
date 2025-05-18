def chkNum(no1):
    if (no1 % 2 == 0):
        print("Even number")
    else :    
        print("Odd number")

def main():
    print("Enter first number")
    no1 = int(input())
   # print("Enter second number ")
    chkNum(no1)
   # chkNum(8)

if __name__=="__main__":
    main()