# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        ## S1: DFS
        ## T: O(N)
        ## S: O(logN)

        self.res = 0
        # use DFS to calculate the depth from node x
        # here depth is the number of nodes from x to a leaf
        # the number of edges from x to leaf is actually depth minus 1

        def dfs(node):
            if not node:
                return 0

            l = dfs(node.left)
            r = dfs(node.right)

            self.res = max(self.res, l + r)
            max_depth = 1 + max(l, r)
            return max_depth

        dfs(root)
        return self.res

        """
        ## S2: DFS

        def dfs(node):
            if node is None:
                return 0
            nonlocal max_diameter
            # Recursively find the depths of the left and right subtrees.
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)
            # Update the maximum diameter found so far.
            # Diameter at this node will be the sum of depths of left & right subtrees.
            max_diameter = max(max_diameter, left_depth + right_depth)
            # Return the depth of this node which is max of left or right subtree depths plus 1.
            return 1 + max(left_depth, right_depth)

        # Initialize the maximum diameter as 0.
        max_diameter = 0
        # Start the DFS traversal from the root.
        dfs(root)
        # Finally, return the maximum diameter found.
        return max_diameter
        """