import threading
import os

def Capitalcount(inputdata):
    count = 0
    print("PID os capitalcount is :",os.getpid())
    print("Thread name is :",threading.current_thread().name)

    for x in range(len(inputdata)):

        if (inputdata[x].isupper() == True):
            count = count + 1
    print("Number of Capital letters are :", count)

def Smallcount(inputdata):
    count = 0
    print("PID os Smallcount is :",os.getpid())
    print("Thread name is :",threading.current_thread().name)

    for x in range(len(inputdata)):

        if(inputdata[x].islower() == True):
            count = count + 1
    print("Number of Small letters are :", count)


def Digitalcount(inputdata):
    count = 0
    print("PID os Digitalcount is :",os.getpid())
    print("Thread name is :",threading.current_thread().name)

    for x in range(len(inputdata)):

        if(inputdata[x].isdigit() == True):
            count = count + 1
    print("Number of Digital letters are :", count)    

def main():

    print("Enter size of elements :") 
    num = int(input())

    print("Enter the numeric values")

    data = []
    for i in range(num):
        data.append(input())


    Capital = threading.Thread(target = Capitalcount, args=(data,))
    Small = threading.Thread(target = Smallcount, args=(data,))
    Digital  = threading.Thread(target = Digitalcount, args=(data,))

    Capital.start()
    Small.start()   
    Digital.start()

    Capital.join()
    Small.join()
    Digital.join()

    print("Exit from main")

if __name__=="__main__":
    main()  