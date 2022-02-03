# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

def print_triangle(n):
    for i in range(1, n + 1):
        for j in range(i):
            print(i, end=" ")
        print()


# *
# ***
# *****
# *******
# *********

def print_star(n):
    for i in range(n, 0, -1):
        for j in range(2 * i - 1):
            print("*", end="")
        print()


def print_star_gyaku(n):
    for i in range(1, n + 1):
        for j in range(2 * i - 1):
            print("*", end="")
        print()
    for i in range(n - 1, 0, -1):
        for j in range(2 * i - 1):
            print("*", end="")
        print()


# palindrome: "", "a", "aba", "abcba"
# not palindrome: "abcde"

# s = ""
# if s == "":
#     pass

# for i in range(len(s)):
# s[i]

def check_palindrome(s):
    if s == "":
        print("palindrome")
    else:
        flag = True
        for i in range(len(s) // 2 + 1):
            if s[i] != s[len(s) - i - 1]:
                flag = False
                break
        if flag == True:
            print("palindrome")
        else:
            print("not palindrome")
