# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        ## S1: BFS

        queue = deque([root])
        max_sum = float('-inf')
        level, res = 0, 0
      
        while queue:
            level += 1
            cur_sum = 0
            # Process all the nodes at the current level
            for _ in range(len(queue)):
                node = queue.popleft()
                cur_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # Update max_sum and res if the current level's sum is greater than max_sum
            if max_sum < cur_sum:
                max_sum, res = cur_sum, level
      
        return res
