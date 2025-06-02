def Display(no):
    if no == 0:
        return
    Display(no-1)
    print(no, end =" ")

def main():
    print("Enter to print values")
    num = int(input())

    Display(num)

if __name__ == "__main__":
    main()