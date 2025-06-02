Fact = 1
def Factorial(no):
    global Fact
    if (no >=1):
        Fact = Fact * no
        no = no-1
        print(no)
        Factorial(no)
    return Fact

def main():
    print("Enter the number of factorial")
    a = int(input())
    ret = Factorial(a)
    print("Factorial is :", ret)

if __name__ == "__main__":
    main()