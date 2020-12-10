#Runtime: 12 ms, faster than 99.59% of
#Python online submissions for Longest Common Prefix.

#Memory Usage: 12.7 MB, less than 84.83% of
#Python online submissions for Longest Common Prefix.

def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if strs == []:
        return ""
    ans = ""
    compare = strs[0]
    for j in range(len(compare)):
        for i in strs:
            try:
                if i[j] != compare[j]:
                    return ans
            except:
                return i
        ans += compare[j]
    return ans
         

print(longestCommonPrefix(["flower","flow","flowht"]))
            
