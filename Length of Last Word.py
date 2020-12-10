#Runtime: 16 ms, faster than 74.29% of Python online
#submissions for Length of Last Word.

#Memory Usage: 13.9 MB, less than 12.76% of Python online
#submissions for Length of Last Word.

def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    start = len(s)-1
    count = 0
    if s[len(s)-1] == " ":
        while s[start] == " ":
            start -= 1
            if start < 0:
                return 0
    for i in range(start, -1, -1):
        if s[i] != " ":
            count += 1
        else:
            break
    return count

print(lengthOfLastWord("  Hello  dude  "))
