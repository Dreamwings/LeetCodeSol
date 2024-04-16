# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:

        ## S2:
        ## T: O(H) ~ O(logN)
        ## S: O(1)

        if not root: return None

        res = root.val

        while root:
            res = min(root.val, res, key=lambda x: (abs(target - x), x))
            if target < root.val:
                root = root.left
            else:
                root = root.right

        return res



        ## S1: Two Boundaries
        ## T: O(H) ~ O(logN)
        ## S: O(1)
        
        if not root: return None
        upper, lower = root.val, root.val
        
        while root:
            if target > root.val:
                lower = root.val
                root = root.right
            elif target < root.val:
                upper = root.val
                root = root.left
            else:
                return root.val
        
        if abs(target - lower) <= abs(target - upper):
            return lower
        return upper
        
