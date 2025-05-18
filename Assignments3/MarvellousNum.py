def chkPrime(no):
    ans = True
    i = 2
    while (i < no):
        if(no % i == 0):
            ans = False
            break
        i = i + 1

    return ans