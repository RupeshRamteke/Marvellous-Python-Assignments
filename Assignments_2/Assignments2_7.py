def main():
    print("Enter size for print pattern :")
    size = int(input())+ 1

    for x in range(1,size):
        for j in range(1,size):
            print(j,end=" ")
        print("\n")    

if __name__=="__main__":
    main()