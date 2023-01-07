# Write your code below this line 👇

def prime_checker(number):
    check = []
    for x in range(2, n):
        result = n % x
        check.append(result)
    # print(check)
    if n > 1 and 0 not in check:
        print("It's a prime number")
    else:
        print("It's not a prime number")


# Write your code above this line 👆
# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
