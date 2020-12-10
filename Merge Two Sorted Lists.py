#Runtime: 32 ms, faster than 40.73% of
#Python online submissions for Merge Two Sorted Lists.

#Memory Usage: 12.6 MB, less than 91.87% of
#Python online submissions for Merge Two Sorted Lists.

"""
FOR LINKED LISTS: TO CREATE, CREATE BOTH A LIST NODE AND
ANOTHER VARIABLE WITH IT TO POINT TO THE NEXT THING (ans_tmp)
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None and l2 == None:
            return None
        elif l1 == None:
            return l2
        elif l2 == None:
            return l1
        elif l1.val < l2.val:
            ans = ListNode(l1.val)
            l1 = l1.next
        else:
            ans = ListNode(l2.val)
            l2 = l2.next
        ans_tmp = ans
        while l1 != None and l2 != None:
            if l1.val > l2.val:
                ans_tmp.next = ListNode(l2.val)
                ans_tmp = ans_tmp.next
                l2 = l2.next
            else:
                ans_tmp.next = ListNode(l1.val)
                ans_tmp = ans_tmp.next
                l1 = l1.next
        if l1 != None:
            while l1 != None:
                ans_tmp.next = ListNode(l1.val)
                ans_tmp = ans_tmp.next
                l1 = l1.next
        elif l2 != None:
            while l2 != None:
                ans_tmp.next = ListNode(l2.val)
                ans_tmp = ans_tmp.next
                l2 = l2.next
        else:
            return ans
        return ans
