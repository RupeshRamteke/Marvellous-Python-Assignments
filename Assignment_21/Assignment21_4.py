import psutil
import Createlog 
import sys
import Sendmail

def ProcessInfo():

    ProcessInfolist = []
    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=['pid','username','name'])
        ProcessInfolist.append(info)

    return ProcessInfolist

def main():


    if(len(sys.argv) ==2):
        if(sys.argv[1] == "--h" or (sys.argv[1] == "--H")):    
            print("This application is used to Create Log file in Directory taking input from user & send mail with attachement")
            print("This is the Directory automation script")

        elif(sys.argv[1] == "--u" or (sys.argv[1] == "--U")):
            print("use the given script as ")
            print("Scriptname.py NameofDirectory mailid")
            print("Please provide valid process name")

        else:
            print("invalid number of arguments")
            print("Use the given flags")
            print("--h : used to display the help")
            print("--u : uses to display teh usage")

    elif(len(sys.argv) == 3):
            
        DirectoryName = sys.argv[1]
        mailID = sys.argv[2]

        RunningProcInfo = ProcessInfo()
        fileInfo = Createlog.generateLogFile(DirectoryName,RunningProcInfo)
        mailInfo = {"subject" : "Running Process Information", "body" : "Please find the attachement"}
        Sendmail.SendmailwithAttachedment(mailID,fileInfo,mailInfo)

    else:
        print("invalid number of argumnets")
        print("Use the given flags")
        print("--h : used to display the help")
        print("--u : uses to display teh usage")


if __name__=="__main__":
    main()    