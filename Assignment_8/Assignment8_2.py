import threading

def evenAdd(no):
    sum = 0
    for x in range(no):
        if (x % 2 ==0):
            sum  = sum + x
    print("Addition of even numbers", sum)

def oddAdd(no):
    sum = 0
    for x in range(no):
        if(x % 2 != 0):
            sum = sum + x
    print("Addition of odd numbers", sum)

def main():

    print("Enter number") 
    num = int(input())

    evenFactor = threading.Thread(target = evenAdd, args=(num,))
    oddFactor = threading.Thread(target=oddAdd, args=(num,))

    evenFactor.start()
    oddFactor.start()   

    evenFactor.join()
    oddFactor.join()

    print("Exit from main")

if __name__=="__main__":
    main()    