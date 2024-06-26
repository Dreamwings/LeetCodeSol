# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        ## S1: DFS
        ## T: O(N)
        ## S: O(H)
        
        if root in {None, p, q}: # Check 3 corner cases
            return root
        
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        
        if l and r: 
            return root
        return l or r  # Otherwise
        

      
        ## S2: DFS
        ## T: O(N)
        ## S: O(H)

        def get_lca(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if not node: 
                return None
            if node in [p, q]: 
                return node
            l, r = get_lca(node.left), get_lca(node.right)
            if l and r: 
                return node
            return l or r

        return get_lca(root)



        ## S3: DFS
        ## T: O(N)
        ## S: O(N)
        
        parents = {}
        
        def dfs(root, parent):
            if not root:
                return
            parents[root] = parent
            dfs(root.left, root)
            dfs(root.right, root)
        
        dfs(root, None)
        
        seen = set()
        while p:
            seen.add(p)
            p = parents[p]
        
        while q:
            if q in seen: return q
            q = parents[q]
