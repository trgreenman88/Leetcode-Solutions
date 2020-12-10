#Runtime: 20 ms, faster than 5.03% of Python online
#submissions for Remove Duplicates from Sorted Array.

#Memory Usage: 14.6 MB, less than 10.28% of Python online
#submissions for Remove Duplicates from Sorted Array.

def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = 0
    previous = ""
    current = nums[0]
    for i in nums:
        if count != 0:
            previous = nums[count-1]
            current = nums[count]
        if previous == current:
            nums.remove(previous)
            nums.insert(0,"*")
        count += 1
    star = nums.count("*")
    for i in range(star):
        nums.remove("*")
    return len(nums)
            
print(removeDuplicates([1,1,2,2]))
