#Runtime: 36 ms, faster than 32.21% of
#Python online submissions for Add Binary.

#Memory Usage: 12.6 MB, less than 99.42% of
#Python online submissions for Add Binary.

def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    num1 = 0
    num2 = 0
    binary = ""
    for i in range(len(a)-1,-1,-1):
        num1 += 2**i * int(a[len(a)-1-i])
    for i in range(len(b)-1,-1,-1):
        num2 += 2**i * int(b[len(b)-1-i])
    ans = num1 + num2
    if ans == 0:
        return "0"
    x = 0
    while 2**x < ans:
        x += 1
    if 2**x > ans:
        x -= 1
    for i in range(x,-1,-1):
        if ans < 2**i:
            binary += "0"
        else:
            binary += "1"
            ans -= 2**i
    
    return binary

print(addBinary("0","0"))
