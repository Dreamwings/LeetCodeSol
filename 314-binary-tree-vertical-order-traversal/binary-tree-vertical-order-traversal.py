# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        ## S1: BFS
        ## T: O(NlogN)
        ## S: O(N)
        
        if not root: return []
        d = defaultdict(list)
        q = deque([(root, 0)])
        
        while q:
            node, x = q.popleft()
            d[x].append(node.val)
            if node.left:
                q.append((node.left, x - 1))
            if node.right:
                q.append((node.right, x + 1))
        
        res = []
        for k in sorted(d):
            res.append(d[k])
        
        return res