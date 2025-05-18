power = lambda a : a*a

def main():
    print ("Enter the value:")
    no = int(input())
    
    result = power(no)

    print("power of number is", result)

if __name__=="__main__":
        main()