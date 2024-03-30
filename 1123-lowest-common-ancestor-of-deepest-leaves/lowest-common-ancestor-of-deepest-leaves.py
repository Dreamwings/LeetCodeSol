# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        ## S1: DFS
        ## T: O(N) for one pass
        ## S: O(H) for recursion management
        
        def dfs(node):
            if not node:
                return None, 0
            
            l_lca, l_depth = dfs(node.left)
            r_lca, r_depth = dfs(node.right)
            
            if l_depth > r_depth:
                return l_lca, l_depth + 1
            elif l_depth < r_depth:
                return r_lca, r_depth + 1
            else:
                return node, l_depth + 1
        
        return dfs(root)[0]