#Runtime: 56 ms, faster than 58.08% of
#Python online submissions for ZigZag Conversion

#Memory Usage: 12.9 MB, less than 32.01% of
#Python online submissions for ZigZag Conversion.

def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    index = 0
    newlist = []
    for i in range(numRows):
        newlist.append([])

    if numRows == 1:
        return s
    i = 0
    while i < len(s):
        if index < numRows-1:
            (newlist[index]).append(s[i])
            index += 1
            i += 1
        elif index == numRows-1:
            while index > 0 and i < len(s):
                (newlist[index]).append(s[i])
                index -= 1
                i += 1
    newstring = ""
    for i in newlist:
        for j in i:
            newstring += j
            
    return newstring

print(convert("HELLODUDE",3))
