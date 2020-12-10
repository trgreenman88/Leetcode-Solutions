"""def sortColors(nums):
    
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    
    count = 0
    i = 0
    while count <= len(nums):
        x = nums[i]
        if nums[i] == 0:
            #Look up how to remove certain index(nums[i])
            nums.remove(x)
            nums.insert(x,0)
            i += 1
        elif nums[i] == 2:
            #Look up how to remove certain index(nums[i])
            nums.remove(x)
            nums.append(x)
        else:
            i += 1
        count += 1
        print(i)
            
    return nums"""

def sortColors(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    count = 0
    i = 0
    store = []
    for i in nums:
        store.append(i)
    while count < len(store):
        if nums[i] == 0:
            nums.insert(0,0)
            i += 2
        elif nums[i] == 2:
            nums.append(2)
            i += 1
        elif nums[i] == 1:
            i += 1
        count += 1
    print(store)
    for i in store:
        if i != 1:
            print(nums)
            nums.remove(i)
            
    return nums

print(sortColors([2,0,2,1,1,0]))
"""
021102 i0
021102 i1
011022 i1
011022 i2
011022 i3
001122 i4
"""

                
