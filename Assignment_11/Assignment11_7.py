
def RightTriangle(no,count):
    
    if(count < no):
        for x in range(count):
            print("*", end=" ")
        print("\n")
        count = count + 1
        RightTriangle(no,count)

def main():
    RightTriangle(5,1)

if __name__ == "__main__":
    main()