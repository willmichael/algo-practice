# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        val1 = l1.val
        val2 = l2.val
        res = val1 + val2
        if res >= 10:
            carry = 1
            res = res % 10

        l3 = ListNode(res)
        l3_head = l3

        l1 = l1.next
        l2 = l2.next

        while(1):
            if l1 == None and l2 == None:
                if carry == 1:
                    l3.next = ListNode(1)
                return l3_head
            elif l1 != None and l2 != None:
                val1 = l1.val
                val2 = l2.val
                res = val1 + val2 + carry
                carry = 0
                if res >= 10:
                    carry = 1
                    res = res % 10

                l3.next = ListNode(res)

                l1 = l1.next
                l2 = l2.next
                l3 = l3.next
            elif l1 == None:
                res = l2.val + carry
                carry = 0
                if res >= 10:
                    carry = 1
                    res = res % 10
                l3.next = ListNode(res)
                l2 = l2.next
                l3 = l3.next
            elif l2 == None:
                res = l1.val + carry
                carry = 0
                if res >= 10:
                    carry = 1
                    res = res % 10
                    print " > 10"
                print carry
                l3.next = ListNode(res)
                l1 = l1.next
                l3 = l3.next

           
