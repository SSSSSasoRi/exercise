def check_prime_number(s):
    flag = True
    for x in range(2, s):
        if s % x == 0:
            print("not prime number")
            flag = False
            break
    if flag == True:
        print("prime number")


s = int(input("number="))
check_prime_number(s)
