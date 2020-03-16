"""
Anh Huynh 025651312
CECS 174 Sec 03
3/11/2020
"""

# get a word from user
def getWord(type):
    word = input("Enter a {}: ".format(type))
    return word

# get an integer from user
def getIn(l1, l2):
    integer = int(input("Enter an integer from {}-{} (inclusive): ".format(l1, l2)))
    return integer

# determine if n is between l1-l2 inclusive
def isValid(n, l1, l2):
    if l1 <= n <= l2:
        return True
    else:
        return False

# returns the inverse of a string
def reverseS(s):
    return s[::-1]

def main():
    pwdict = {    # dictionary library for all the variables
       "word": getWord("word"),
       "symbol": getWord("symbol"), 
       "punctuation": getWord("punctuation"),
       "integer1": getWord("number"),
       "l1": int(input("Enter a lower limit: ")),
       "l2": int(input("Enter an upper limit: ")),
        }

    pwdict["integer2"] = getIn(pwdict["l1"], pwdict["l2"])
    
    while not(isValid(pwdict["integer2"], pwdict["l1"], pwdict["l2"])):    # loop to validate integer
        print("Please enter a valid integer from {}-{} (inclusive): ".format(pwdict["l1"], pwdict["l2"]))
        pwdict["integer2"] = int(input())

    password = (pwdict["symbol"] * pwdict["integer2"]) + pwdict["punctuation"] + pwdict["integer1"] + (pwdict["word"] + pwdict["word"][0:3])    # generate the password
    passwordR = reverseS(password)

    print(password)
    print(passwordR)

main()