import os

def main():
    print("Enter the name of the file")

    filename = input()

    flag = os.path.exists(filename)

    if(flag == False):
        print("Enter valid name of file")
        exit()

    fobj1 = open("Destination.txt", "w")
    fobj2 = open(filename,"r")

    sourcefiledata = fobj2.read()

    fobj1.write(sourcefiledata)

    fobj1.close()
    fobj2.close()


if __name__=="__main__":
    main()
