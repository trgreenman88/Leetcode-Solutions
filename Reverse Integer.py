#Runtime: 40 ms, faster than 8.04% of
#Python online submissions for Reverse Integer.

#Memory Usage: 12.9 MB, less than 6.07% of
#Python online submissions for Reverse Integer.

def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    num = str(x)
    newnum = ""
    if x < 0:
        x = abs(x)
        num = str(x) + "-"
    else:
        num = str(x)
    for i in range(len(num),0,-1):
        newnum += num[i-1]
    if int(newnum) < (-2**31) or int(newnum) > (2**31)-1:
        return 0
    else:
        return int(newnum)

print(reverse(1534236469))
