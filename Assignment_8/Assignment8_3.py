import threading

def evenAdd(no):
    sum = 0
    for x in range(len(no)):

        if (no[x] % 2 ==0):
            sum  = sum + no[x]
    print("Addition of even numbers", sum)

def oddAdd(no):
    sum = 0
    for x in range(len(no)):

        if(no[x] % 2 != 0):
            sum = sum + no[x]
    print("Addition of odd numbers", sum)

def main():

    print("Enter size of elements :") 
    num = int(input())

    print("Enter the numeric values")

    data = []
    for i in range(num):
        data.append(int(input()))

    evenlist = threading.Thread(target = evenAdd, args=(data,))
    oddlist = threading.Thread(target=oddAdd, args=(data,))

    evenlist.start()
    oddlist.start()   

    evenlist.join()
    oddlist.join()

    print("Exit from main")

if __name__=="__main__":
    main()  