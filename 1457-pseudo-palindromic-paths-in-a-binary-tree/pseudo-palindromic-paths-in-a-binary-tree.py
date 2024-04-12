# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        ## S1: Iterative Preorder Traversal (DFS)
        ## T: O(N)
        ## S: O(H)

        count = 0
        
        stack = [(root, 0) ]
        while stack:
            node, path = stack.pop()
            if node is not None:
                # Compute occurences of each digit in the corresponding register
                # XOR is used to compute the digit frequency
                # If a digit appears an odd number of times, we'll get 1's bit in the XOR result
                path = path ^ (1 << node.val)
                # if it's a leaf, check if the path is pseudo-palindromic
                if node.left is None and node.right is None:
                    # check if at most one digit has an odd frequency
                    if path & (path - 1) == 0:
                        count += 1
                else:
                    stack.append((node.right, path))
                    stack.append((node.left, path))
        
        return count

        """

        ## S2: Recursive DFS
        ## T: O(N)
        ## S: O(H)

        def preorder(node, path):
            nonlocal count
            if node:
                # compute occurences of each digit 
                # in the corresponding register
                path = path ^ (1 << node.val)
                # if it's a leaf, check if the path is pseudo-palindromic
                if node.left is None and node.right is None:
                    # check if at most one digit has an odd frequency
                    if path & (path - 1) == 0:
                        count += 1
                else:                    
                    preorder(node.left, path)
                    preorder(node.right, path) 
        
        count = 0
        preorder(root, 0)
        return count

        """