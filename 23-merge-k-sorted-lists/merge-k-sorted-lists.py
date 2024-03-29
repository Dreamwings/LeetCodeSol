# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        from heapq import heapify, heappush, heappop
        
        ## S3: Divide and Conquer
        ## T: O(NlogK)
        ## S: O(1)

        def merge2Lists(l1, l2):
            head = point = ListNode(0)
            while l1 and l2:
                if l1.val <= l2.val:
                    point.next = l1
                    l1 = l1.next
                else:
                    point.next = l2
                    l2 = l1
                    l1 = point.next.next
                point = point.next

            if not l1:
                point.next=l2
            else:
                point.next=l1

            return head.next

        n = len(lists)
        j = 1
        while j < n:
            for i in range(0, n - j, j * 2):
                lists[i] = merge2Lists(lists[i], lists[i + j])
            j *= 2

        return lists[0] if n > 0 else None

        """

        ## S2: Heap (Optimized S1)
        ## T: O(NlogK)
        ## S: O(K)

        hq = []
        # to avoid error from heapq by comparing two nodes when they have the same values
        # add the index i into the tuple
        for i, node in enumerate(lists):
            if node:
                heappush(hq, (node.val, i, node))
        
        dummy = ListNode(0)
        curr = dummy
        
        while hq:
            v, i, x = heappop(hq)
            curr.next = x
            curr = curr.next
            
            if x.next:
                heappush(hq, (x.next.val, i, x.next))
        
        return dummy.next
        
        
        
        ## S1: 

        # need to redefine the operator to compare ListNode, otherwise Python 3 will report errors
        def __lt__(a: ListNode, b: ListNode):
            return a.val < b.val
        ListNode.__lt__ = __lt__

        
        hq = []
        for node in lists:
            if node:
                hq.append((node.val, node))
        
        heapify(hq)
        dummy = ListNode(0)
        curr = dummy
        
        while hq:
            v, x = heappop(hq)
            curr.next = x
            curr = curr.next
            if x.next:
                heappush(hq, (x.next.val, x.next))
            
        return dummy.next
        """
        
        
        