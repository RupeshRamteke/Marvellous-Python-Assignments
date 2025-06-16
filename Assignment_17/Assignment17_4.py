import schedule
import time

def display():
    print("Namaskar")

def main():

    schedule.every().day.at("01:30").do(display)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__=="__main__":
    main()


