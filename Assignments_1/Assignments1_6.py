def chkNum(no1):
    if (no1 > 0):
        print("positive number")
    elif (no1 < 0):
        print("Negative number")
    else:
        print("Zero")


def main():
    print("Enter the number")
    value = int(input())
    
    chkNum(value)

if __name__=="__main__":
    main()