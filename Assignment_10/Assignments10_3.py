from functools import reduce

GreatNum = lambda val : (70 <= val and val <= 90)
Addten = lambda b : (b + 10)
Mul = lambda b,a :(b*a)

def main():
    print ("Enter size of elemants :")
    size = int(input())

    Data = []

    for i in range(size):
        Data.append(int(input()))

    Fdata = list(filter(GreatNum, Data))
    print("Filter data is ", Fdata)

    Mdata = list(map(Addten, Fdata))
    print("Map data is :", Mdata)

    Rdata = reduce(Mul, Mdata)
    print ("Reduce is :", Rdata)

if __name__=="__main__":
    main()
