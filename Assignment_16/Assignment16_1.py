def main():

    fobj = open("student.txt", "w")

    print("Enter the 5 name of stundent in file")

    for x in range(5):
        fobj.write(input())
        fobj.write("\n")


if __name__=="__main__":
    main()
