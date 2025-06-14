import os

def main():

    print("Enter the name of the file")

    filename = input()
 
    flag = os.path.exists(filename)

    if(flag == False):
        print("Enter the valid name")
        exit()

    fobj = open(filename,"r")

    lines = fobj.readlines()

    for line in lines:
        for word in line.split():
            if(word.isnumeric() == False):
                nameofstudent = word
            if(word.isnumeric() == True and int(word) > 75):
                print(nameofstudent)

    fobj.close()


if __name__=="__main__":
    main()
