import MarvellousNum


def ListPrime(number):
    sum = 0

    for x in range(len(number)):
        ans = MarvellousNum.chkPrime(number[x])
        if(ans == True):
            sum = sum + number[x]
    
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


    result = ListPrime(data,)

    print (" Minimum number from list is:", result)

if __name__=="__main__":
        main()    