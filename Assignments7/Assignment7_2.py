doub = lambda a : a*2

def main():
    print("Enter the number of elements")
    num = int(input())

    print("Enter numeric values:")
    data = []

    for i in range(num):
        data.append(int(input()))

    Mdata = list(map(doub,data))
    print("Mapt data is :")
    print(Mdata)

if __name__=="__main__":
    main()