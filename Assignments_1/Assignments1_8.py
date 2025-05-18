def display(no):
    for no in (range(no)):
        print("*",end=" ")


def main():
    
    print("Enter the size")
    no = int(input())

    display(no)

if __name__=="__main__":
    main()