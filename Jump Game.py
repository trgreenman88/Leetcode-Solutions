def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    print(nums)
    if len(nums) == 0:
        return True
    for i in nums:
        if i != 0:
            return canJump(nums[i:])
        for j in range(1,i+1):
            return canJump(nums[nums.index(i)+j:])
    #return False

print(canJump([3,2,1,0,4]))
