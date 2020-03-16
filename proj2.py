"""
ANH HUYNH 025651312
CECS 174 SEC 03
2/27/20
"""

def main():
    # inputs and counters
    bot_int = int(input("Enter an integer: "))
    top_int = int(input("Enter another integer: "))
    palin_count = 0
    nonlych_count = 0
    lych_count = 0
   
    for i in range(bot_int, top_int + 1):
        # palindrome counter
        if is_palindrome(i):
            palin_count += 1

        # nonlych counter
        if is_nonlychrel(i):
            nonlych_count += 1  

        # lych counter
        if is_lychrel(i):
            lych_count += 1      

    # final outputs
    print("""\n*************\n
In the range of {} to {},
Palindrome count: {}
Non-lychrel count: {}
Lychrel count: {}""".format(bot_int, top_int, palin_count, nonlych_count - lych_count, lych_count))

# test if a var is a palindrome
def is_palindrome(num):
    num = str(num)
    new_var = num[::-1]

    if new_var == num:
        return True
    else:
        return False
        
# test if a var is a nonlyrchrel
def is_nonlychrel(num):
    if is_palindrome(num):
        return False
    
    num = str(num)
    new_var = num[::-1]
    counter = 0

    while not(is_palindrome(int(num))):
        num = int(num) + int(new_var)
        new_var = str(num)[::-1]
        counter += 1

        if counter >= 60:
            return True

    else:
        return True

# test if a var is a lychrel and return the value
def is_lychrel(num):
    if is_palindrome(num):
        return False
    
    og_num = num
    num = str(num)
    new_var = num[::-1]
    counter = 0

    while not(is_palindrome(int(num))):
        num = int(num) + int(new_var)
        new_var = str(num)[::-1]
        counter += 1

        if counter >= 60:
            print("{} looks like a lychrel number.".format(og_num))
            return True

main()