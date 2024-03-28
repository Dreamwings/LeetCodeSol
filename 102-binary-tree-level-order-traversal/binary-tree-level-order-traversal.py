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
        
        """
        ## S2: Recursive BFS

        levels = []
        if not root:
            return levels
        
        def helper(node, level):
            # start the current level
            if len(levels) == level:
                levels.append([])

            # append the current node value
            levels[level].append(node.val)

            # process child nodes for the next level
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)
            
        helper(root, 0)
        return levels
        """