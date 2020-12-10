def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    sizen = len(needle)
    sizeh = len(haystack)
    for i in range(sizeh):
        compare = ""
        for j in range(sizen):
            if haystack[i+j] == needle[j]:
                compare += needle[j]
            if compare == needle:
                return i

print(strStr("wrigley field","ey"))
