# ----------------------------------------------------------------
# https://leetcode.com/discuss/interview-question/506608/Sink-zeroes-in-a-Binary-Tree
# https://www.techiedelight.com/sink-nodes-containing-zero-bottom-binary-tree/
# ----------------------------------------------------------------

# A class to store a binary tree node
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sink_zeros_in_binary_tree(root: TreeNode) -> None:

        ## S1: DFS + Stack
        ## T: O(N)
        ## S: O(H) ~ O(N) for worst case

        stack = []
        num_zeros = 0

        def dfs(node):
            if not node:
                return

            nonlocal num_zeros

            if not node.val:
                num_zeros += 1
            else:
                stack.append(node.val)

            dfs(node.left)
            dfs(node.right)

            if num_zeros:
                num_zeros -= 1
                node.val = 0
            else:
                node.val = stack.pop()

        dfs(root)
