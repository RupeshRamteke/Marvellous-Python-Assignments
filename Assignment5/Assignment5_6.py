def main():

    print("Enter temperature in celcius : ")
    temp = int(input())

    F = (temp * (9/5)) + 32

    print("Temperature in Fahreneit : ",F)

if __name__=="__main__":
    main()