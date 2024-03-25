# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        ## S2:  Iterative BFS
        ## Time: O(N)
        ## Space: O(N)
        
        from collections import deque
        
        if not root: return 0
        
        res = 0
        q = deque([root])
        
        while q:
            x = q.popleft()
            if low <= x.val <= high:
                res += x.val
            if x.left and x.val > low:
                q.append(x.left)
            if x.right and x.val < high:
                q.append(x.right)
        
        return res
        
        """
        ## S1: Recursive DFS
        ## Time: O(N)
        ## Space: O(N)
        
        res = 0
        if not root: return res
        
        if low <= root.val <= high:
            res += root.val
        
        l = self.rangeSumBST(root.left, low, high)
        r = self.rangeSumBST(root.right, low, high)
        
        return res + l + r
        
        """
        
     