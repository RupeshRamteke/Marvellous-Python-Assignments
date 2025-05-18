def Maximum(number):
    sum = 0

    for x in range(len(number)):
        if(number[x] > sum):
            sum = number[x]
    
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

    result = Maximum(data)

    print ("Maximum number from list is:", result)

if __name__=="__main__":
        main()    