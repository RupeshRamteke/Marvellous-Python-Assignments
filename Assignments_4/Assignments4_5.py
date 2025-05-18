from functools import reduce

def prime(val):
    ans = True
    i = 2
    while (i < val):
        if(val % i == 0):
            ans = False
            break
        i = i+1

    if(ans == True):
        return ans
    
def multiplication(val):
    mult = val*2
    return mult

def Maximum(val1, val2):
    if(val1 < val2):
        return val2
    else:
        return val1    


def main():
    print ("Enter size of elemants :")
    size = int(input())

    Data = []

    for i in range(size):
        Data.append(int(input()))

    Fdata = list(filter(prime, Data))
    print("Filter data is ", Fdata)

    Mdata = list(map(multiplication, Fdata))
    print("Map data is :", Mdata)

    Rdata = reduce(Maximum, Mdata)
    print ("Reduce is :", Rdata)

if __name__=="__main__":
    main()
