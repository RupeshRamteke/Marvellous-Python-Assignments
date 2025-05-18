from functools import reduce

Even = lambda val : ( val % 2 == 0)
Square = lambda b : (b*b)
Add = lambda b,a :(b+a)

def main():
    print ("Enter size of elemants :")
    size = int(input())

    Data = []

    for i in range(size):
        Data.append(int(input()))

    Fdata = list(filter(Even, Data))
    print("Filter data is ", Fdata)

    Mdata = list(map(Square, Fdata))
    print("Map data is :", Mdata)

    Rdata = reduce(Add, Mdata)
    print ("Reduce is :", Rdata)

if __name__=="__main__":
    main()
