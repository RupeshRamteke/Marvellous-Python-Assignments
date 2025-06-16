import schedule
import time

def display():
    print("Jai ganesh")


def main():

    schedule.every(2).seconds.do(display)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__=="__main__":
    main()


