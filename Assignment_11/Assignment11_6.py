sum = 0

def Natural(no):
    global sum
    if(no > 0):
        sum = sum + no
        no = no - 1
        Natural(no)
    return sum

def main():
    print("Enter the number for addition of natural number: ")
    a = int(input())
    ret = Natural(a)
    print(ret)

if __name__ == "__main__":
    main()