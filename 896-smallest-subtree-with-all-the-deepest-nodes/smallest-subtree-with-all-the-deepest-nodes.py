# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        
        ## S1: DFS
        ## T: O(N)
        ## S: O(H)

        def dfs(node):
            # return the LCA of all deepest nodes and the depth from the current 
            # node to the deepest nodes
            # return (lca, depth)
            
            if not node:
                return None, 0
            
            l, l_depth = dfs(node.left)
            r, r_depth = dfs(node.right)
            
            if l_depth > r_depth:
                return l, l_depth + 1
            elif l_depth < r_depth:
                return r, r_depth + 1
            else:
                return node, l_depth + 1
        
        res, _ = dfs(root)
        return res
        