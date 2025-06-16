import schedule
import datetime
import time


def Lunch():
    print("Lunch time :")

def Logout():
    print("Wrap up time:")
    

def main():

    schedule.every().day.at("13:00").do(Lunch)
    schedule.every().day.at("18:00").do(Logout)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()


