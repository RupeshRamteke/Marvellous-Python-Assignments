import time
import os

def CreatelogFile(Foldername, data):

    Flag = os.path.exists(Foldername)

    if(Flag == False):
        os.mkdir(Foldername)

    timestamp = time.ctime()
    timestamp = timestamp.replace(" ","")
    timestamp = timestamp.replace(":","_")
    timestamp = timestamp.replace("/","_")

    Filename = os.path.join(Foldername, "Marvellous%s.log" %(timestamp))

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

def generateLogFile(foldername, data):

    flag = os.path.exists(foldername)

    if(flag == False):
        os.mkdir(foldername)

    timestamp = time.ctime()
    timestamp = timestamp.replace(" ","")
    timestamp = timestamp.replace(":","_")
    timestamp = timestamp.replace("/","_")

    name = "Marvellous%s.log" %timestamp
    Filename = os.path.join(foldername, "MArvellous%s.log" %(timestamp))

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

    fileInfo = {"name" : name, "path": Filename}

    return fileInfo



