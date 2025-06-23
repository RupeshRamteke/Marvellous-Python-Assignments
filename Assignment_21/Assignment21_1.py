import psutil
import Createlog 

def Dispalyprocess():

    ProcessInfolist = []
    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=['pid','username','name'])
        ProcessInfolist.append(info)

    return ProcessInfolist

def main():

    ProcessInformation = Dispalyprocess()
    Createlog.CreatelogFile("LogDirectoryAssignment21_1", ProcessInformation)

if __name__=="__main__":
    main()