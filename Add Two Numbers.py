def uniquePaths(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    pathsdict = {}
    def Paths(m,n):
        if (m,n) in pathsdict.keys():
            return pathsdict[(m,n)]
        if m == 1 and n == 1:
            value = 1
        else:
            if m == 1:
                value = Paths(m, n-1)
            elif n == 1:
                value = Paths(m-1, n)
            else:
                value = Paths(m-1, n) + Paths(m, n-1)
        pathsdict[(m,n)] = value
        return value

    ans = Paths(m,n)
    return ans


print(uniquePaths(3,2))




