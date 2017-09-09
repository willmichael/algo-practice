# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return []
        o_head = head
        stack = []
        for i in range(k):
            if not head:
                return o_head
            stack.append(head)
            head = head.next
        
        new_head = stack.pop()
        cur = new_head
        while stack:
            new_head.next = stack.pop()
            new_head = new_head.next
        new_head.next = head
        return cur
            
