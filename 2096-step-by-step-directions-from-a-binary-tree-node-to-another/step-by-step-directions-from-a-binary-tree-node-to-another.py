# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        ## S1: DFS
        ## https://algo.monster/liteproblems/2096
        ## T: O(N)
        ## S: O(N)

        # Buidl the string in reverse order to avoid creating new copy
        def dfs(root: Optional[TreeNode], val: int, path: List[chr]) -> bool:
            if root.val == val:
                return True
            if root.left and dfs(root.left, val, path):
                path.append('L')
            elif root.right and dfs(root.right, val, path):
                path.append('R')
            return len(path) > 0

        path_to_start = []
        path_to_dest = []

        dfs(root, startValue, path_to_start)
        dfs(root, destValue, path_to_dest)

        while path_to_start and path_to_dest and path_to_start[-1] == path_to_dest[-1]:
            path_to_start.pop()
            path_to_dest.pop()

        return 'U' * len(path_to_start) + ''.join(reversed(path_to_dest))