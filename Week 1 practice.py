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

stringReverser()