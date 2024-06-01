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
	/	  \
   1	   0

Output:

	   1
	 /   \
	/	  \
   0	   0

Example 2:
Input:

	   0
	 /	 \
	/	  \
   /	   \
  1			0
		   / \
	 	  /	  \
		 0	   2
		/ \
	   /   \
	  3		4

Output:

	   1
	 /	 \
	/	  \
   /	   \
  0			3
		   / \
	 	  /	  \
		 4	   2
		/ \
	   /   \
	  0		0

or any other valid binary tree.
"""


# A class to store a binary tree node
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sink_zeros_in_binary_tree(root: TreeNode) -> None:

        ## S2: DFS (By ChatGPT)
        ## T: O(N)
        ## S: O(H) ~ O(N) for worst case

        if not node:
            return
        
        # Sink zeros in the left and right subtrees first
        sink_zeros(node.left)
        sink_zeros(node.right)
        
        # If current node is zero, we need to sink it down
        if node.val == 0:
            if node.left and node.left.val != 0:
                # Swap values with the left child if it's non-zero
                node.val, node.left.val = node.left.val, node.val
                # Recursively sink the zero in the left subtree
                sink_zeros(node.left)
            elif node.right and node.right.val != 0:
                # Swap values with the right child if it's non-zero
                node.val, node.right.val = node.right.val, node.val
                # Recursively sink the zero in the right subtree
                sink_zeros(node.right)
            # If both children are zero or non-existent, zero remains at this node



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
