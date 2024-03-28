# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        ## S1: BFS
        ## T: O(N)
        ## S: O(N)
        
        if not root: return []
        
        res = []
        q = [root]
        
        while q:
            cur = []
            vals = []
            for node in q:
                vals.append(node.val)
                if node.left:
                    cur.append(node.left)
                if node.right:
                    cur.append(node.right)
            q = cur
            res.append(vals)
        
        return res
        