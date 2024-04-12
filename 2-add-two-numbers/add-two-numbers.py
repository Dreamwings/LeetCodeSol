# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        ## S2:

        c = 0
        dummy = ListNode(-1)
        p = dummy

        while l1 or l2 or c:
            s = c + (l1.val if l1 else 0) + (l2.val if l2 else 0)
            c, s = s // 10, s % 10
            p.next = ListNode(s)
            p = p.next
            s = 0
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

        """

        ## S1:

        s, c = 0, 0
        
        dummy = ListNode(-1)
        p = dummy
        
        # add the two linked list for each node
        while l1 or l2:
            s += c
            if l1:
                s += l1.val
                l1 = l1.next
            if l2:
                s += l2.val
                l2 = l2.next
            
            c = s // 10
            s = s % 10
            p.next = ListNode(s)
            p = p.next
            s = 0
        
        if c: p.next = ListNode(c)
        
        return dummy.next

        """