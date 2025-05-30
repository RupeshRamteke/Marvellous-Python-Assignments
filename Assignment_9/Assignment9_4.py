import time
import threading
import multiprocessing

def Addition():
    sum = 0
    for x in range(0,10000000):
        sum = sum + x
    print("Addition is ", sum)

def main():
    start_time = time.time()
    result = Addition()

    end_time = time.time()
    print("Execution time for normal function :",end_time-start_time)

    thread_start_time = time.time()
    T1 = threading.Thread(target = Addition)
    T1.start()
    T1.join()
    thread_end_time = time.time()
    print("Execution time for thread ", thread_end_time-thread_start_time)

    multiprocess_start_time = time.time()
    p1 = multiprocessing.Process(target = Addition)
    p1.start()
    p1.join()

    multiprocess_end_time = time.time()
    print("Execution time for multiprocessing" ,multiprocess_end_time - multiprocess_start_time)

if __name__=="__main__":
    main()    