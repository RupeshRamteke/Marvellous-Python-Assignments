def main():
    i = 1
    sum = 0
    while(i <= 100):
        if (i % 2 == 0):
            sum = sum + i
        i = i + 1

    print("sum of even number between 1 to 100 :", sum)    

if __name__=="__main__":
    main()