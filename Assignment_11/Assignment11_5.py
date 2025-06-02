Count = 0

def count_zero(no):
    global Count
    if(no > 0):
        y = no % 10
        if (y == 0):
            Count = Count + 1
        no = no // 10
        count_zero(no)
    return Count

def main():
    print("Enter the number to count zero: ")
    a = int(input())
    ret = count_zero(a)
    print(ret)

if __name__ == "__main__":
    main()