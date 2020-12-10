#Runtime: 32 ms, faster than 23.05% of
#Python online submissions for Remove Nth Node From End of List.

#Memory Usage: 12.9 MB, less than 22.60% of
#Python online submissions for Remove Nth Node From End of List.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        i = head
        length = 0
        while i != None:
            i = i.next
            length += 1
        k = length - n
        prev = None
        current = head
        for i in range(k):
            prev = current
            current = current.next
        if prev == None:
            return head.next
        else:
            prev.next = current.next
            current.next = None
        return head
