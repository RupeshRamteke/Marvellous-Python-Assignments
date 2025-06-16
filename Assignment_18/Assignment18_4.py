import os
import sys 

def main():

    if(len(sys.argv) ==2):
        if(sys.argv[1] == "--h" or sys.argv == "--H"):
            print("This script is use to compare the content of both file are same")
        elif(sys.argv[1] == "--u" or sys.argv == "--U"):
            print("Used the given script as")
            print("Scripname.py Argument1 Arguments2")
        else:
            print("Inalid number of arugumnet")
            print("Used the given flag is")
            print("--h : Used ti display help")
            print("--u :Used to dispaly the usage")
    elif(len(sys.argv) ==3):
        filename1 = sys.argv[1]
        filename2 = sys.argv[2]

        flag = os.path.exists(filename1)        

        if(flag == False):
            print(filename1, "There is no such file, please enter the valid name" ,end=" ")
            exit()
                  
        flag = os.path.exists(filename2,)
        if(flag == False):
            print(filename2, "There is no such file, please enter the valid name" ,end=" ")
            exit()

        fobj1= open(filename1,"r")
        fobj2 = open(filename2,"r")

        data1 = fobj1.read()
        data2 = fobj2.read()

        if(data1 == data2):
            print("Success")
        else:
            print("failure")    

        fobj1.close()
        fobj2.close()

    else:
        print("Inalid number of arugumnet")
        print("Used the given flag is")
        print("--h : Used ti display help")
        print("Used to dispaly the usage")   

if __name__=="__main__":
    main()            