

def main():

    print("Enter the number of line")
    size =int(input())

    fobj = open("Number.txt", "w")

    for x in range(size):
        fobj.write(input())
        fobj.write("\n")
    
    fobj.close()

if __name__=="__main__":
    main()
