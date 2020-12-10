#Runtime: 16 ms, faster than 76.54% of
#Python online submissions for Climbing Stairs.

#Memory Usage: 12.9 MB, less than 11.13% of
#Python online submissions for Climbing Stairs.

def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    a = 1
    b = 1
    for i in range(n):
        a, b = b, a+b
    return a

print(climbStairs(40))
        
