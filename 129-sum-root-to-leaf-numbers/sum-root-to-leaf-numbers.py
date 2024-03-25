# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        ## S3: DFS
        ## T: O(N)
        ## S: O(H)

        def dfs(node, ans) -> int:
            if not node:
                return 0
            ans = ans * 10 + node.val
            if not node.left and not node.right:
                return ans
            return dfs(node.left, ans) + dfs(node.right, ans)
        return dfs(root, 0)    
        """

        ## Solution 1: BFS
        ## T: O(N)
        ## S: O(N)
        
        q = [(root, root.val)]
        vals = []
        
        while q:
            next_q = []
            for node, v in q:
                if not node.left and not node.right:
                    vals.append(v)
                if node.left:
                    next_q.append((node.left, v * 10 + node.left.val))
                if node.right:
                    next_q.append((node.right, v *10 + node.right.val))
                
            q = next_q
        
        return sum(vals)
        
        ## S2: DFS
        ## T: O(N)
        ## S: O(N)

        q = [(root, root.val)]
        res = 0
        
        while q:
            node, v = q.pop()
            if not node.left and not node.right:
                res += v
            
            if node.left:
                q.append((node.left, v * 10 + node.left.val))
            if node.right:
                q.append((node.right, v * 10 + node.right.val))
        
        return res
        """
        