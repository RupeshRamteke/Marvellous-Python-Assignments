def main():
    print("Enter number :")
    x = int(input())

    i = 0
    while (x > 0):
        i = i + 1
        x = x//10

    print ("The digit of number is", i)    

if __name__=="__main__":
    main()