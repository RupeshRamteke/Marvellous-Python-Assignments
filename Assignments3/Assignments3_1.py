def Addition(number):
    sum = 0

    for x in range(len(number)):
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

    result = Addition(data)

    print ("addition of all elements in list is:", result)

if __name__=="__main__":
        main()    