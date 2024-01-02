# Week 1 practice
# reverse string
# input string, output string


def stringReverser():
    print("Enter your string")
    yourString = input()
    reversedString = ""
    for x in reversed(yourString):
        reversedString += x
    print(reversedString)

# stringReverser()
    
# Substring problem
# Write a function that takes in two strings and returns true if the second string is substring of the first, and false otherwise.
def subStringer():
    print("Input your string")
    yourString = input()
    print("Now input the substring")
    yourSubString = input()
    if(yourSubString in yourString):
        print(True)
        return
    print(False)
    return False

subStringer()

# Next prime number
def prime_finder(n):
    if n <= 1:
        return 2
    n += 1
    while True:
        if is_prime(n):
            return n
        n += 1

def is_prime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
