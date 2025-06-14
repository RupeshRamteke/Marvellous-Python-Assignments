import os

def main():

    print("Open the file only in reading mode")
    filename = input()

    flag = os.path.exists(filename)
    if(flag == False):
        print("Enter the valid file name")
        exit()

    fobj = open(filename,"r")

    data = fobj.read()

    print("File contents are as follow")
    print(data)

    fobj.close()

if __name__=="__main__":
    main()
