import threading
import time

def display():
    for x in range(1,6):
        print(x, end = " ")
    print("\n")

def main():

    T1 = threading.Thread( target = display)
    T2 = threading.Thread( target = display)
    T3 = threading.Thread( target = display)

    T1.start()
    time.sleep(1)
    T2.start()
    time.sleep(1)
    T3.start()
    time.sleep(1)

    T1.join()
    T2.join()
    T3.join()

if __name__=="__main__":
    main()    