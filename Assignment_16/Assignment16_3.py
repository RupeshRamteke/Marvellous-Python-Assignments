import os

def main():

    print("Enter the name of the file")
    filename = input()

    flag = os.path.exists(filename)
    if(flag == False):
        print("Enter the valis file name")
        exit()

    fobj = open(filename,"r")

    linecount = 0
    wordcount = 0
    char = 0

    lines = fobj.readlines()

    for line in lines:
        linecount = linecount + 1
        for word in line.split():
            wordcount = wordcount + 1
            for i in word:
                char = char + 1

    fobj.close()            
    
    print("line count is : ",linecount)
    print("Word count is : ",wordcount)
    print("Charcters count is :",char)


if __name__=="__main__":
    main()
