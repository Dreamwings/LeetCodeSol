# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        ## S3: DFS
        ## T: O(N)
        ## S: O(H)
        def dfs(node):
            if not node: return

            if low <= node.val <= high:
                self.total_sum += node.val
            if node.val > low:
                dfs(node.left)
            if node.val < high:
                dfs(node.right)

        self.total_sum = 0
        dfs(root)
        return self.total_sum



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
        


        ## S4:  Iterative DFS
        ## Time: O(N)
        ## Space: O(N)
 
        ans = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if low <= node.val <= high:
                    ans += node.val
                if low < node.val:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
        return ans