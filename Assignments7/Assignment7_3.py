even = lambda a : (a % 2 == 0)

def main():
    print("Enter number of elements")
    num = int(input())

    print("Enter numeric values:")
    data = []

    for i in range(num):
        data.append(int(input()))

    Fdata = list(filter(even,data))
    print("Filter data is :")
    print(Fdata)

if __name__=="__main__":
    main()