def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    dictlist = []
    ans = []
    addstring = ""
    dictionary = {
        "2": ["a","b","c"],
        "3": ["d","e","f"],
        "4": ["g","h","i"],
        "5": ["j","k","l"],
        "6": ["m","n","o"],
        "7": ["p","q","r","s"],
        "8": ["t","u","v"],
        "9": ["w","x","y","z"]
    }
    length = 1
    for i in range(len(digits)):
        length *= len(dictionary[digits[i]])
    print(length)
    while digits != "":
        dictlist.append(dictionary[digits[0]])
        digits = digits[1:]
    print(dictlist)
    while length > 0:
        for i in range(len(dictlist)):
            count = length % (len(dictlist[i]))
            addstring += dictlist[i][count]
        ans.append(addstring)
        addstring = ""
        length -= 1
        #print(ans)
    return ans
        
    
                    
print(letterCombinations("23"))
