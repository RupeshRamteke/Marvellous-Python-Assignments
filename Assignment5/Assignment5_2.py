def main():

    print("Enter alphabet")
    val1 = input()

    print("-------------")

    if( val1 == "a" or val1 == "e" or val1 == "i" or val1 == "o" or val1 == "u") :
        print(val1, "is vowel")

    else:
        print(val1, "is consonant")    
if __name__=="__main__":
    main()
