def Division (no1):
    if (no1%5 == 0): 
        return True
    else:
        return False

def main():
    print("Enter the number")
    value = int(input())
    
    result = Division(value)

    print(result)

if __name__=="__main__":
    main()