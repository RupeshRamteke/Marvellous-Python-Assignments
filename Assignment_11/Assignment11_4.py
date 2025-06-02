powerNum = 1

def power(no,p):
    global powerNum
    if(p > 0):
        y = no%10
        powerNum = powerNum * no
        p = p-1
        power(no,p)
    return powerNum

def main():
    print("Enter the number : ")
    base = int(input())
    print("Enter raise to number : ")
    raiseNum = int(input())
    ret = power(base,raiseNum)
    print(ret)

if __name__ == "__main__":
    main()