# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        from collections import defaultdict
        """
        ## S1: BFS
        ## T: O(NlogN)
        ## S: O(N)

        if not root: return []
        
        d = defaultdict(list)
        res = []
        q = [(root, 0)]
        
        while q:
            nxt = []
            t = defaultdict(list)
            for node, i in q:
                t[i].append(node.val)
                if node.left:
                    nxt.append((node.left, i-1))
                if node.right:
                    nxt.append((node.right, i+1))
            
            q = nxt
            for k, v in t.items():
                d[k] += sorted(v)
        
        for k in sorted(d):
            res.append(d[k])
        
        return res

        """
        ## S2: DFS

        nodes = []
        def dfs(node, r, c):
            if node:
                nodes.append([r, c, node.val])
                dfs(node.left, r+1, c-1)
                dfs(node.right, r+1, c+1)
            return
        
        dfs(root, 0, 0)
        nodes = sorted(nodes, key=lambda x:(x[1], x[0], x[2]))
        d = defaultdict(list)
        for i, j, k in nodes:
            d[j].append(k)
        res = []
        for i in d.values():
            res.append(i)
        return res