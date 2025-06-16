import os
import sys 

def main():

    if(len(sys.argv) ==2):
        if(sys.argv[1] == "--h" or sys.argv == "--H"):
            print("This script is used to calculate the frequency of word in file")
        elif(sys.argv[1] == "--u" or sys.argv == "--U"):
            print("Used the given script as")
            print("Scripname.py Argument1 Arguments2")
        else:
            print("Invalid number of arugumnet")
            print("Used the given flag is")
            print("--h : Used ti display help")
            print("--u :Used to dispaly the usage") 

    elif(len(sys.argv) == 3):
        filename = sys.argv[1]
        inputword = sys.argv[2]

        fobj = open(filename, "r")

        count = 0

        linesinfile = fobj.readlines()

        for x in linesinfile:
            for word in x.split():
                if(inputword == word):
                    count = count + 1
        
        fobj.close()

        print(inputword, ": Total count is", count, "in" , filename, end= " ")

    else:
        print("Invalid number of arugumnet")
        print("Used the given flag is")
        print("--h : Used ti display help")
        print("--u :Used to dispaly the usage")    


if __name__=="__main__":
    main()            