# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        ## S1: DFS + DFS Backtracking
        ## T: O(N)
        ## S: O(N)
        
        ## find parent nodes and store in dict, then do DFS backtracking
        res = []
        if not root: return res
        # dict for parent nodes, key: value = node.val : parent
        parents = collections.defaultdict(TreeNode)

        def find_parent(node):
            if node.left:
                parents[node.left.val] = node
                find_parent(node.left)
            if node.right:
                parents[node.right.val] = node
                find_parent(node.right)
        
        find_parent(root)
        seen = set()
        # now using dfs with backtracking to find nodes with dist k

        def dfs(curr, dist):
            seen.add(curr)
            if dist == 0:
                res.append(curr.val)
                return
            
            next_nodes = [curr.left, curr.right]
            if curr.val in parents:
                next_nodes.append(parents[curr.val])
            
            for node in next_nodes:
                if node and node not in seen:
                    dfs(node, dist - 1)

        dfs(target, k)

        return res



        """
        ## S2: DFS + DFS Backtracking
        
        if not root: return []
        
        parents = collections.defaultdict(TreeNode)

        def find_parent(node):
            if node.left:
                parents[node.left.val] = node
                find_parent(node.left)
            if node.right:
                parents[node.right.val] = node
                find_parent(node.right)
        
        find_parent(root)
        res = []

        def dfs(curr, prev, dist):
            if dist == 0:
                res.append(curr.val)
                return
            
            # the following lines can also use a for loop
            if curr.left and curr.left != prev:
                dfs(curr.left, curr, dist - 1)
            if curr.right and curr.right != prev:
                dfs(curr.right, curr, dist - 1)
            if curr.val in parents and parents[curr.val] != prev:
                dfs(parents[curr.val], curr, dist - 1)
        
        dfs(target, None, k)
        return res
    
        
        ## S3: DFS + BFS
        
        if not root: return []
        
        # use DFS to build graph
        graph = collections.defaultdict(list)
        
        def dfs(root):
            if root.left:
                graph[root.val].append(root.left.val)
                graph[root.left.val].append(root.val)
                dfs(root.left)
            if root.right:
                graph[root.val].append(root.right.val)
                graph[root.right.val].append(root.val)
                dfs(root.right)
        
        dfs(root)
        
        # do BFS to find nodes with dist of K
        seen = set()
        q = [target.val]
        seen.add(target.val)
        
        for _ in range(k):
            nxt = []
            for x in q:
                for y in graph[x]:
                    if y not in seen:
                        nxt.append(y)
                        seen.add(y)
            q = nxt
        
        return q
        """
        
        