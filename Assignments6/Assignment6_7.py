def main():
    print("Enter elements number")
    size = int(input())

    data = []

    print("Enter numeric value")
    for x in range(size):
        ele = int(input())
        data.append(ele)

    print(data)    

    max = 0

    for no in range(len(data)):
        if(data[no] > max):
            max = data[no]

    print ("Maximum number from all elements in list is ", max)        

if __name__=="__main__":
    main()