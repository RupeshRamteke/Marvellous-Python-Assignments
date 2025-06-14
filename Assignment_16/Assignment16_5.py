import os

def main():
    print("Enter the file name to read")
    filename = input()

    flag = os.path.exists(filename)
    if(flag == False):
        print("Enter valid file name")
        exit()

    fobj = open(filename,"r")

    count = 0
    
    linesinfile = fobj.readlines()

    for x in linesinfile:
        count = 0
        for word in x.split():
            count = count + 1
            if(count > 5):
                print(x)
                break

    fobj.close()        

if __name__=="__main__":
    main()
