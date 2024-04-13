# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        ## S1: Level BFS
        ## T: O(N)
        ## S: O(N)
        
        if not root: return []
        
        res = []
        q = [root]
        
        while q:
            nxt = []
            max_v = float('-inf')
            for x in q:
                max_v = max(x.val, max_v)
                if x.left:
                    nxt.append(x.left)
                if x.right:
                    nxt.append(x.right)
            res.append(max_v)
            q = nxt
        return res
    
        """
        ## S2: BFS
        ## T: O(N)
        ## S: O(N)
        
        res = []
        if not root: return res
        
        q = [(root, 1)]
        
        while q:
            x, idx = q.pop()
            if len(res) < idx:
                res.append(float('-inf'))
            
            res[idx-1] = max(res[idx-1], x.val)
            
            if x.left:
                q.append((x.left, idx + 1))
            if x.right:
                q.append((x.right, idx + 1))
        
        return res    
        """    
        
