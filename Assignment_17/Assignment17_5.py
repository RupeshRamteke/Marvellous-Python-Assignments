import schedule
import datetime
import time


def display():

    fobj = open("MArvellous.txt", "a")
    currenttime = str(datetime.datetime.now())
    fobj.write(currenttime)
    fobj.write("\n")
    
    fobj.close()

def main():

    schedule.every(2).minutes.do(display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()


