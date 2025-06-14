import os

def main():

    print("Enter the name of file")

    filename = input()

    flag = os.path.exists(filename)
    if(flag == False):
        print("Enter the valid name")
        exit()

    fobj = open(filename, "r")

    fobj1 = open("XYZ.txt","w")
    
    lines = fobj.readlines()

    for line in lines:
        if line.strip() == "":
            continue
        else:
            fobj1.write(line)

    fobj.close()
    fobj1.close()

if __name__=="__main__":
    main()    


