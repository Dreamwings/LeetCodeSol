# ----------------------------------------------------------------
# https://leetcode.com/discuss/interview-question/506608/Sink-zeroes-in-a-Binary-Tree
# https://www.techiedelight.com/sink-nodes-containing-zero-bottom-binary-tree/
# ----------------------------------------------------------------

"""
Given the root of a binary tree containing many zero nodes, sink nodes having 
zero value at the bottom of the subtree rooted at that node. In other words, 
the resultant binary tree should not contain any node having zero value that 
is the parent of the node having a non-zero value.

Since several binary tree might satisfy the constraints, the solution should 
return any one of them.
Example 1:
Input:

           0
         /   \
        /     \
       1       0

Output:

           1
         /   \
        /     \
       0       0

Example 2:
Input:

           0
	 /   \
	/     \
       1       0
	      /  \
	     /	  \
	    0	   2
	   / \
	  /   \
	 3     4

Output:
           1
	 /   \
	/     \
       0       3
	      /  \
	     /	  \
	    4	   2
	   / \
	  /   \
	 0     0

or any other valid binary tree.
"""


# A class to store a binary tree node
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sink_zeros(root: TreeNode) -> None:

        ## S2: DFS (By ChatGPT)
        ## T: O(N)
        ## S: O(H) ~ O(N) for worst case

        if not root:
            return None

        # Recursively sink zeros in the left and right subtrees
        root.left = sink_zeros(root.left)
        root.right = sink_zeros(root.right)

        # If root is zero, we need to sink it
        if root.val == 0:
            if root.left and root.left.val != 0:
                # Swap root with left child if left child is non-zero
                root.val, root.left.val = root.left.val, root.val
                root.left = sink_zeros(root.left)
            elif root.right and root.right.val != 0:
                # Swap root with right child if right child is non-zero
                root.val, root.right.val = root.right.val, root.val
                root.right = sink_zeros(root.right)

        return root




        ## S1: DFS + Stack
        ## T: O(N)
        ## S: O(H) ~ O(N) for worst case

        stack = []
        num_zeros = 0

        def dfs(node):
            if not node:
                return

            nonlocal num_zeros

            if not node.val:  # Zero value
                num_zeros += 1
            else:  # Non-zero value
                stack.append(node.val)

            dfs(node.left)
            dfs(node.right)

            if num_zeros:
                num_zeros -= 1
                node.val = 0
            else:
                node.val = stack.pop()

        dfs(root)
