#Runtime: 6792 ms, faster than 6.66% of
#Python online submissions for Valid Parentheses.

#Memory Usage: 539.2 MB, less than 5.48% of
#Python online submissions for Valid Parentheses.

def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    if s == "":
        return True
    array = list(s)
    #print(array)
    for i in range(len(array)):
        if array[i] == ")":
            if array[i-1] == "(":
                del array[i-1]
                del array[i-1]
                string = ""
                for i in array:
                    string += i
                return isValid(string)
            else:
                return False
        if array[i] == "]":
            if array[i-1] == "[":
                del array[i-1]
                del array[i-1]
                string = ""
                for i in array:
                    string += i
                return isValid(string)
            else:
                return False
        if array[i] == "}":
            if array[i-1] == "{":
                del array[i-1]
                del array[i-1]
                string = ""
                for i in array:
                    string += i
                return isValid(string)
            else:
                return False

print(isValid("(]"))


