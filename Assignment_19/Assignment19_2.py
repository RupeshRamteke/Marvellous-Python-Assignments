import os
import sys
import time


def Createlog(Foldername, data):

    Flag = os.path.exists(Foldername)

    if(Flag == False):
        os.mkdir(Foldername)

    timestamp = time.ctime()
    timestamp = timestamp.replace(" ","")
    timestamp = timestamp.replace(":","_")
    timestamp = timestamp.replace("/","_")

    Filename = os.path.join(Foldername, "MArvellous%s.log" %(timestamp))

    Fobj = open(Filename, "w")

    border = "-"*80
    Fobj.write(border)
    Fobj.write("\n\t\tMarvellous infosystem Process Log\n")
    Fobj.write("\t\tLog file is created at : "+time.ctime()+"\n")
    Fobj.write(border)
    Fobj.write("\n")

    for x in data:
        Fobj.write("%s \n" %x)

    Fobj.write(border)
    Fobj.close()


def NewFileExtension(DirectoryName, Oldextension, NewExtension):

    flag = os.path.isabs(DirectoryName)
    if(flag == False):
        DirectoryName = os.path.abspath(DirectoryName)

    flag = os.path.exists(DirectoryName)    
    if(flag == False):
        print("Path is Invalid")
        exit() 

    flag = os.path.isdir(DirectoryName)
    if(flag == False):
        print("Path is valid bu the target is not Directory")   
        exit() 

    Filelist = []

    for foldernames, subfilenames, filename in os.walk(DirectoryName):
        for file in filename:
            if(file.endswith(Oldextension)):
                replaceextension = file.replace(Oldextension, NewExtension)

                name = os.path.join(foldernames,file)
                SFname = os.path.join(foldernames,replaceextension)

                os.rename(name,SFname)
                Filelist.append(file)

    return Filelist

def main():

    Border = "-"*84
    print(Border)
    print("-----------------Marvellous-----------------")
    print(Border)

    if(len(sys.argv) ==2):
        if(sys.argv[1] == "--h" or (sys.argv[1] == "--H")):    
            print("This application is used to change the file extension:")
            print("This is the Directory automation script")

        elif(sys.argv[1] == "--u" or (sys.argv[1] == "--U")):
            print("use the given script as ")
            print("Scriptname.py NameofDirectory NameoffileExtension NameofNewfileExtension")
            print("Please provide valid absolute path")

        else:
            print("invalid number of command line argumnets")
            print("Use the given flags")
            print("--h : used to display the help")
            print("--u : uses to display teh usage")

    elif(len(sys.argv) == 4):
        DirectoryName = sys.argv[1]
        Oldextension = sys.argv[2]
        NewExtension = sys.argv[3]

        Filelist = NewFileExtension(DirectoryName, Oldextension,NewExtension)
        Createlog("FileAutomationlog",Filelist)


    else:
        print("invalid number of command line argumnets")
        print("Use the given flags")
        print("--h : used to display the help")
        print("--u : uses to display teh usage")


if __name__=="__main__":
    main()    