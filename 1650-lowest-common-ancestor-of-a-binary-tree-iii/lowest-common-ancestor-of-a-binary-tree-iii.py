"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, A: 'Node', B: 'Node') -> 'Node':
        
        ## S2: Two Pointers
        ## Time: O(logN) 
        ## Space: O(1)

        pa, pb = A, B
        while pa != pb:
            pa = pa.parent if pa.parent else B
            pb = pb.parent if pb.parent else A

        return pa

        """
        ## S1:
        ## Time: O(logN) 
        ## Space: O(logN)
        # note that it doesn't give the root
        # first traverse from one of the node to root and store nodes in the path
        path = set()
        while A:
            path.add(A)
            A = A.parent

        while B:
            if B in path:
                return B
            B = B.parent

        return None
        """
        