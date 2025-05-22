rev = lambda x : x == reversed(x)

def main():
    print("Enter string")
    str = input()

    res= rev(str)

    if(res):
        print(str," is Palimdrom")
    else:
        print(str," is not Palimdrom")


if __name__ == "__main__":
    main()