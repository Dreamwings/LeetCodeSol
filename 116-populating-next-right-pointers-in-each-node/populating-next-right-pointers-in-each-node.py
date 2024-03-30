"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        ## S2: Level BFS
        ## T: O(N)
        ## S: O(N)
        
        if not root: return None
        
        q = [root]
        
        while q:
            nxt = []
            q.append(None)
            for x, y in zip(q[:-1], q[1:]):
                x.next = y
                if x.left:
                    nxt.append(x.left)
                    nxt.append(x.right)
            
            q = nxt
        
        return root
        
        """
        #               1
        #       2               3
        #   4       5  -->  6       7
        # 8   9->10  11-->12  13->14  15        
        
        ## S1:
        ## T: O(N)
        ## S: O(1)

        if not root: return None
        
        p = root
        p.next = None
        
        while p and p.left:
            p_next = p.left
            while p:
                p.left.next = p.right
                if p.next == None:
                    p.right.next = None
                else:
                    p.right.next = p.next.left
                p = p.next  # level traversal to finish this level with while loop
            
            p = p_next # depth traversal
        
        return root
        

        """