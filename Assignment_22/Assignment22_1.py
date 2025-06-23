import os
import Mychecksum
import time 
import schedule
import Createlog
import Sendmail
import sys

def CheckDuplicatefiles(DirectoryName):

    flag = os.path.isabs(DirectoryName)

    if(flag == False):
        DirectoryName = os.path.abspath(DirectoryName)

    flag = os.path.exists(DirectoryName)    

    if(flag == False):
        print("Please enter valid name of Directory")
        exit() 

    Duplicate = {}    
    totalNumScanned = 0

    for foldername , subfoldernames, filenames in os.walk(DirectoryName):
        for fname in filenames:
            fname = os.path.join(foldername,fname)
            totalNumScanned = totalNumScanned + 1
            checksum = Mychecksum.calculaltechecksum(fname)
            if checksum in Duplicate:
                Duplicate[checksum].append(fname)
            else:
                Duplicate[checksum] = [fname]

    return Duplicate , totalNumScanned

def DeleteDuplicate(path, mailID):

    timestamp = time.ctime()
    
    resultArr , totalcnt = CheckDuplicatefiles(path)

    result = list(filter(lambda x : len(x) >0 , resultArr.values()))

    
    DelFileNameList = []
    DeleteFilecnt = 0
    checkSumCnt = 0

    for value in result:
        for subvalue in value:
            checkSumCnt = checkSumCnt + 1
            if(checkSumCnt > 1):
                DelFileNameList.append(subvalue)
                os.remove(subvalue)
                DeleteFilecnt = DeleteFilecnt + 1
        
        checkSumCnt = 0


    #Log file function
    FileInfo = Createlog.generateLogFile("Marvellous",DelFileNameList)

    #sendmail
    mailbody = "Starting time of scanning" +timestamp+"\n Toatal file Scanned:" + str(totalcnt)+"\n Total number of duplicate File found :" +str(DeleteFilecnt)

    mailInfo = {"subject" : "Duplcate file(s) delete log", "body": mailbody}
    Sendmail.SendmailwithAttachedment(mailID, FileInfo, mailInfo)


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

    elif(len(sys.argv) == 4):
            
        DirectoryName = sys.argv[1]
        timeinterval = int(sys.argv[2])
        recievermaild = sys.argv[3]

        schedule.every(timeinterval).minutes.do(DeleteDuplicate,DirectoryName,recievermaild)

        while True:
            schedule.run_pending()
            time.sleep(1)


    else:
        print("invalid number of argumnets")
        print("Use the given flags")
        print("--h : used to display the help")
        print("--u : uses to display teh usage")


if __name__=="__main__":
    main()       
