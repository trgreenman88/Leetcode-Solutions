#Runtime: 196 ms, faster than 5.16% of
#Python online submissions for Median of Two Sorted Arrays.

#Memory Usage: 12.8 MB, less than 89.08% of
#Python online submissions for Median of Two Sorted Arrays.

def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    newlist = []
    for i in nums1:
        newlist.append(i)
    for i in nums2:
        newlist.append(i)
    newlist.sort()
    if len(newlist)%2 == 1:
        median = newlist[len(newlist)//2]
    else:
        median = (newlist[len(newlist)//2] + newlist[len(newlist)//2 - 1])*0.5
    return median

print(findMedianSortedArrays([1,2],[3,4]))

def findMedianSortedArrays2(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    size = len(nums1) + len(nums2)
    nums = nums1 + nums2
    print(nums)

print(findMedianSortedArrays2([1,2],[3,4]))
