import schedule
import time

def backup():
    fobj = open("logfile.txt", "a")
    fobj.write("Taking backup \n")
    fobj.close()

def main():

    schedule.every(1).hour.do(backup)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()
