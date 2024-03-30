# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        
        ## S1: DFS + Cache
        ## T: O(2^(N/2))
        ## S: O(2^(N/2))

        from functools import lru_cache

        @lru_cache(None)
        def buildFBT(total_nodes):
            if total_nodes == 1:
                return [TreeNode()]
          
            # List to store all unique FBTs created from 'total_nodes' nodes.
            full_binary_trees = []
          
            # Iterate over the number of nodes left after one is taken as the current root.
            for nodes_in_left_subtree in range(total_nodes - 1):
                nodes_in_right_subtree = total_nodes - 1 - nodes_in_left_subtree
              
                # Generate all full binary trees for the number of nodes in left subtree.
                left_subtrees = buildFBT(nodes_in_left_subtree)
                # Generate all full binary trees for the number of nodes in right subtree.
                right_subtrees = buildFBT(nodes_in_right_subtree)
              
                # Combine each left subtree with each right subtree and add the current node as root.
                for left in left_subtrees:
                    for right in right_subtrees:
                        full_binary_trees.append(TreeNode(0, left, right))
          
            # Return the list of all unique full binary trees.
            return full_binary_trees

        
        return buildFBT(n)
        


        """

        ## S2: DP
        ## T: O(2^(N/2))
        ## S: O(2^(N/2))

        if n % 2 == 0:
            return []

        dp = [[] for _ in range(n + 1)]
        dp[1].append(TreeNode(0))
        
        for count in range(3, n + 1, 2):
            for i in range(1, count - 1, 2):
                j = count - 1 - i
                for left in dp[i]:
                    for right in dp[j]:
                        root = TreeNode(0, left, right)
                        dp[count].append(root)

        return dp[n]

        """