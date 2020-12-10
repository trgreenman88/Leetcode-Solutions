#Runtime: 80 ms, faster than 18.65% of
#Python online submissions for Palindrome Number.

#Memory Usage: 12.7 MB, less than 54.58% of
#Python online submissions for Palindrome Number.

def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0:
        return False
    string = str(x)
    for i in range(len(string)//2 + 1):
        if string[i] != string[len(string)-1-i]:
            return False
    return True

print(isPalindrome(121))
