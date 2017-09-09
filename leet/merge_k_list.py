# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = cur = ListNode(0)
        n_lists = [] 
        for li in lists:
            if li: n_lists.append(li)
        while n_lists:
            val = {} 
            for idx, nl in enumerate(n_lists):
                if nl: val[nl.val] = idx
            if len(val) > 0:
                idx = val[min(val.keys())]
                cur.next = n_lists[idx]
                cur = cur.next
                n_lists[idx] = n_lists[idx].next
            else:
                break
        return head.next

