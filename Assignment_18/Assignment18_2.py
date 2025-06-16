def main():

    print("Enter the name of the file to check in Directory")

    filename = input()

    Fobj = open(filename, "r")
    
    Data = Fobj.read()

    Fobj.read()

    print(Data)
    
if __name__=="__main__":
    main()