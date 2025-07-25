import sys
import hashlib
import os
import Createlog
import time

def checkSumFile(files, blocksize):
    
    fobj= open(files, "rb")

    hobj = hashlib.md5()
    buffer = fobj.read(blocksize)
    while(len(buffer)>0):
        hobj.update(buffer)
        buffer = fobj.read()

        fobj.close()

    return hobj.hexdigest()

def CalculatecheckSum(DirectoryName):

    flag = os.path.isabs(DirectoryName)

    if(flag == False):
        DirectoryName = os.path.abspath(DirectoryName)

    flag = os.path.exists(DirectoryName)

    if(flag == False):
        print("Path in Invalid")
        exit()

    flag = os.path.isdir(DirectoryName)

    if(flag == False):
        print("Path is valid but target is not Directory")

    Checksumfilelist = {}

    for Foldernames, subfoldername, filenames in os.walk(DirectoryName):
        for filename in filenames:
            filename = os.path.join(Foldernames,filename)
            Checksum = checkSumFile(filename, 1024)
            if Checksum in Checksumfilelist:
                Checksumfilelist[Checksum].append(filename)
            else:
                Checksumfilelist[Checksum] = [filename]

    return Checksumfilelist

def DuplicateFilelist(MyDict):

    timestamp = time.time()

    Result = list(filter(lambda x : len(x) > 1, MyDict.values()))

    x = []
    count = 0
    cnt = 0
    
    for value in Result:
        for subvalue in value:
            count = count + 1
            if(count > 1):
                print("Delete files :", subvalue)
                x.append(subvalue)
                os.remove(subvalue)
                cnt = cnt + 1
        count = 0

    endtime = time.ctime()

    TotalTime = (time.time() - timestamp)
    x.append(TotalTime)
    
    print("Total deleted files", cnt)

    return x


def main():

    if(len(sys.argv) ==2):
        if(sys.argv[1] == "--h" or (sys.argv[1] == "--H")):    
            print("This application is used to Display checkSum of files:")
            print("This is the File IO automation script")

        elif(sys.argv[1] == "--u" or (sys.argv[1] == "--U")):
            print("use the given script as ")
            print("Scriptname.py NameofDirectory ")
            print("Please provide valid absolute path")

        else:
            DirectoryName = sys.argv[1]
            checkSumInfo = CalculatecheckSum(DirectoryName)
            deletelogfile = DuplicateFilelist(checkSumInfo)
            
            Createlog.CreatelogFile("Assignment20", deletelogfile)

    else:
        print("invalid number of command line argumnets")
        print("Use the given flags")
        print("--h : used to display the help")
        print("--u : uses to display teh usage")


if __name__=="__main__":
    main()