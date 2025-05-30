import threading
import os

def displayord():
    for x in range(1,51):
        print (x, end = " ")
    print("\n")

def displayrev():
    for x in range(50,0,-1):
        print (x, end = " ")
    print ("\n")  

def main():

    thread1 = threading.Thread(target = displayord, args = ())      
    thread2 = threading.Thread(target = displayrev, args = ())

    thread1.start()
    thread1.join()

    thread2.start()
    thread2.join()

if __name__=="__main__":
    main()