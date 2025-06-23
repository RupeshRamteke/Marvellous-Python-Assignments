import psutil
import Createlog 
import sys

def ProcessInfo():

    ProcessInfolist = []
    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=['pid','username','name'])
        ProcessInfolist.append(info)

    return ProcessInfolist

def main():

    Border = "-"*84
    print(Border)
    print("-----------------Marvellous-----------------")
    print(Border)

    if(len(sys.argv) ==2):
        if(sys.argv[1] == "--h" or (sys.argv[1] == "--H")):    
            print("This application is used to Create Log file in Directory taking input from user:")
            print("This is the Directory automation script")

        elif(sys.argv[1] == "--u" or (sys.argv[1] == "--U")):
            print("use the given script as ")
            print("Scriptname.py NameofDirectory")
            print("Please provide valid absolute path")

        else:
            DirectoryName = sys.argv[1]

            Runingprocess = ProcessInfo()
            Createlog.CreatelogFile(DirectoryName,Runingprocess)

    else:
        print("invalid number of command line argumnets")
        print("Use the given flags")
        print("--h : used to display the help")
        print("--u : uses to display teh usage")


if __name__=="__main__":
    main()    