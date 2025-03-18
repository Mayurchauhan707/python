def ispalindrome(str):
    str.lower()
    return True if str==str[::-1]else False
str="MADAM"
print(ispalindrome(str))
str="nayan"
print(ispalindrome(str))
