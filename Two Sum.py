#Runtime: 4292 ms, faster than 24.97% of
#Python online submissions for Two Sum.

#Memory Usage: 13.6 MB, less than 69.40% of
#Python online submissions for Two Sum.

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]

print(twoSum([3,3], 6))
    
