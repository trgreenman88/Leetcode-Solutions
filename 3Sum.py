#Time Limit Exceeded
"""
def threeSum(nums):
    
    :type nums: List[int]
    :rtype: List[List[int]]
    
    nums.sort()
    solns = []
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                if nums[i] + nums[j] + nums[k] == 0 and [nums[i],nums[j],nums[k]] not in solns:
                    solns.append([nums[i],nums[j],nums[k]])
    return solns
    """

#Time Limit Exceeded
def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums.sort()
    ans = []
    for i in range(len(nums)-2):
        if nums[i] > 0:
            return ans
        pointer1 = i + 1
        pointer2 = len(nums)-1
        while pointer1 < pointer2:
            if nums[i] + nums[pointer1] + nums[pointer2] == 0 and [nums[i],nums[pointer1],nums[pointer2]] not in ans:
                ans.append([nums[i],nums[pointer1],nums[pointer2]])
                while pointer1 < pointer2 and nums[pointer1] == nums[pointer1+1]:
                    pointer1 += 1
                while pointer1 < pointer2 and nums[pointer2] == nums[pointer2-1]:
                    pointer2 -= 1
                pointer1 += 1
                pointer2 -= 1
            elif nums[i] + nums[pointer1] + nums[pointer2] < 0:
                pointer1 += 1
            else:
                pointer2 -= 1
            
            
    return ans
            
        

print(threeSum([-1,0,1,2,-1,-4]))
