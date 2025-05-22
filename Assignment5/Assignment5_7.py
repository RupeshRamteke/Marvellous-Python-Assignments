def main():
    print("Enter length : ")
    len = int(input())

    print ("Enter width : ")
    width = int(input())

    Area = len * width
    print ("Area is : ",Area)

    perimeter = 2 * (len + width)
    print("Perimeter is :", perimeter)


if __name__=="__main__":
    main()