# Palindrome- A number, word or phrase that reads the same in the forwards and backwards way
def isPalindrome(string):
    if not isinstance(string, (str, float, int)):
        return False
    string=string.lower()
    new_string="".join(char for char in string if char.isalnum())
    is_pal=new_string == new_string[::-1]
    return is_pal

s=['apple', 'apple', 'apple']
print(isPalindrome(s))
