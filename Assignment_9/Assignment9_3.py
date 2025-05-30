import multiprocessing

def factorial(no):
    result = 1
    for x in range(no,0,-1):
        result = result * x
    return result

def main():

    print("Enter size of data")
    size = int(input())

    data = []

    print("Enter numeric values")

    for x in range (size):
        data.append(int(input()))

    p = multiprocessing.Pool()
    Mdata = []

    Mdata = p.map(factorial, data)
    p.close()
    p.join()

    print(Mdata)

if __name__=="__main__":
    main()    