#Runtime: 96 ms, faster than 96.88% of
#Python online submissions for Container With Most Water.

#Memory Usage: 14 MB, less than 26.83% of
#Python online submissions for Container With Most Water.

def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    """areas = [0]
    for j in range(1,len(height)+1):
        for i in range(1,len(height)+1):
            areas.sort()
            if height[i-1] >= height[j-1]:
                area = abs(height[j-1]*(i-j))
                if area >= areas[-1]:
                    areas.append(area)
    return(areas[-1])"""
    
    index1 = 0
    index2 = len(height)-1
    pointer1 = height[index1]
    pointer2 = height[index2]
    if pointer1 > pointer2:
        area = (index2-index1)*pointer2
    else:
        area = (index2-index1)*pointer1
    while index2 > index1:
        if height[index1] > height[index2]:
            index2 -= 1
            pointer2 = height[index2]
        else:
            index1 += 1
            pointer1 = height[index1]
        if pointer1 > pointer2 and (index2-index1)*pointer2 > area:
            area = (index2-index1)*pointer2
        elif pointer2 >= pointer1 and (index2-index1)*pointer1 > area:
            area = (index2-index1)*pointer1
    return area
        
        
print(maxArea([1,8,6,2,5,4,8,3,7]))
