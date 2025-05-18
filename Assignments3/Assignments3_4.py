def Freqnum(number,Searchnum):
    sum = 0

    for x in range(len(number)):
        if(number[x] == Searchnum):
            sum = sum + 1
    
    return sum

def main():
    print("Enter elements number")
    size = int(input())

    data = []

    print("Enter numeric value")

    for x in range(size):
        element = int(input())
        data.append(element)

    print(data)

    print("Element to search")
    checknum = int(input())

    result = Freqnum(data,checknum)

    print (" Minimum number from list is:", result)

if __name__=="__main__":
        main()    