def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    plist = []
    pstring = ""
    for i in range(n):
        pstring += "()"
    plist += pstring
    return plist
        
