import os

def main():
    
    print("Enter the file name name that you want to check")
    filename = input()

    ret = os.path.exists(filename)

    if(ret == True):
        print("File exists in Directory")

    else:
        print("There is no such file")

if __name__=="__main__":
    main()            
