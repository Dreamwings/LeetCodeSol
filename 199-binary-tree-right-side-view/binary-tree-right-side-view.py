# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        ## S2: Iterative BFS
        ## T: O(N)
        ## S: O(D) ~ O(N) for worst case, D is max width of all levels
        
        res = []
        if not root: return res
        
        q = []
        q.append(root)
        
        while q:
            nxt = []
            for node in q:
                x = node.val
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            res.append(x)
            q = nxt
        
        return res
        

        
        ## S1: Recursive DFS
        ## T: O(N)
        ## S: O(H) ~ O(N) for worst case, H is tree height
        
        res = []
        if not root: return res
        
        res.append(root.val)
        
        l = self.rightSideView(root.left)
        r = self.rightSideView(root.right)
        
        res += r
        
        return res + r + l[len(r):]

        