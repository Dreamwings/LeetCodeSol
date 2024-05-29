# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        ## S3: Recursive DFS (Note S4 is Optimal)
        ## T: O(N)
        ## S: O(H) ~ O(N) for worst case

        self.res = 0
        def dfs(node, cur_v):
            if not node:
                return
            # Calculate the current val from root to node
            cur_v = cur_v * 10 + node.val
            # If the current node is a leaf, add the current val to the result
            if not node.left and not node.right:
                self.res += cur_v
            # If not a leaf, continue DFS
            dfs(node.left, cur_v)
            dfs(node.right, cur_v)

        dfs(root, 0)
        return self.res

        # Another writing to aviod global variable
        # def dfs(node, res) -> int:
        #     if not node:
        #         return 0
        #     res = res * 10 + node.val
        #     if not node.left and not node.right:
        #         return res
        #     return dfs(node.left, res) + dfs(node.right, res)
            
        # return dfs(root, 0)


        ## S4: Morris Algorithm Preorder Traversal 
        ## T: O(N)
        ## S: O(1)

        res = cur_val = 0
        
        while root:  
            # If there is a left child,
            # then compute the predecessor.
            # If there is no link predecessor.right = root --> set it.
            # If there is a link predecessor.right = root --> break it.
            if root.left: 
                # Predecessor node is one step to the left 
                # and then to the right till you can.
                p = root.left 
                steps = 1
                while p.right and p.right is not root: 
                    p = p.right 
                    steps += 1

                # Set link predecessor.right = root
                # and go to explore the left subtree
                if p.right is None:
                    cur_val = cur_val * 10 + root.val                    
                    p.right = root  
                    root = root.left  
                # Break the link predecessor.right = root
                # Once the link is broken, 
                # it's time to change subtree and go to the right
                else:
                    # If you're on the leaf, update the sum
                    if p.left is None:
                        res += cur_val
                    # This part of tree is explored, backtrack
                    for _ in range(steps):
                        cur_val //= 10
                    p.right = None
                    root = root.right 
                    
            # If there is no left child
            # then just go right.        
            else: 
                cur_val = cur_val * 10 + root.val
                # if you're on the leaf, update the sum
                if root.right is None:
                    res += cur_val
                root = root.right
                        
        return res

        

        ## Solution 1: BFS
        ## T: O(N)
        ## S: O(D) ~ O(N)
        
        q = [(root, root.val)]
        vals = []
        
        while q:
            next_q = []
            for node, v in q:
                if not node.left and not node.right:
                    vals.append(v)
                if node.left:
                    next_q.append((node.left, v * 10 + node.left.val))
                if node.right:
                    next_q.append((node.right, v *10 + node.right.val))
                
            q = next_q
        
        return sum(vals)
        
        ## S2: Iterative DFS
        ## T: O(N)
        ## S: O(N)

        q = [(root, root.val)]
        res = 0
        
        while q:
            node, v = q.pop()
            if not node.left and not node.right:
                res += v
            
            if node.left:
                q.append((node.left, v * 10 + node.left.val))
            if node.right:
                q.append((node.right, v * 10 + node.right.val))
        
        return res
        
        