# Trying to solve the palindrome number question on leetcode

def ispalindrome(x):
    if str(x) == str(x)[::-1]:
        return True
    else:
        return False
    
print(ispalindrome(121))