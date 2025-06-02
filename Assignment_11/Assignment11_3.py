sum = 0
def Sum_of_Digit(no):
    global sum
    if(no > 0):
        y = no%10
        sum = sum + y
        no = no // 10
        Sum_of_Digit(no)
    return sum

def main():
    print("Enter the number of for addition of digits: ")
    a = int(input())
    ret = Sum_of_Digit(a)
    print(ret)

if __name__ == "__main__":
    main()