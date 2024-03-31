# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        ## S1: BFS
        
        if not root: return []
        q = [(root, root.val, [root.val])]
        res = []
        
        for node, path_sum, path in q:
            if path_sum == targetSum and not node.left and not node.right:
                res.append(path)
            if node.left:
                q.append((node.left, path_sum + node.left.val, path + [node.left.val]))
            if node.right:
                q.append((node.right, path_sum + node.right.val, path + [node.right.val]))
        
        return res
              

        """
        ## S2: DFS
        
        if not root: return []
        if root.val == targetSum and not root.left and not root.right: return [[root.val]]
        
        l = self.pathSum(root.left, targetSum - root.val)
        r = self.pathSum(root.right, targetSum - root.val)
        
        res = []
        for x in l:
            res.append([root.val] + x)
        
        for y in r:
            res.append([root.val] + y)
        
        return res
        """
