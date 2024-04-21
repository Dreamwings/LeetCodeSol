# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        ## S1: DFS
        ## T: O(N)
        ## S: O(N)

        def dfs(node, cur_depth):
            # If node is None (the base case), we have reached a leaf's child and we return
            if node is None:
                return
          
            # If we have reached the desired depth, we add the new row with val
            if cur_depth == depth - 1:
                node.left = TreeNode(val, left=node.left, right=None)
                node.right = TreeNode(val, left=None, right=node.right)
                return
          
            # Recursively call DFS on the left and right children, incrementing the depth
            dfs(node.left, cur_depth + 1)
            dfs(node.right, cur_depth + 1)

        # Special case when the new row needs to be added at the root
        if depth == 1:
            return TreeNode(val, left=root)
      
        dfs(root, 1)
        return root

        

        ## S2: BFS
        ## T: O(N)
        ## S: O(N)

        if depth == 1:
            return TreeNode(val, root, None)
        
        q = deque([root])
        while q and depth != 1:
            depth -= 1
            for _ in range(len(q)):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                
                if depth == 1: # Current level is in depth depth-1 -> Add nodes with value `val`
                    curr.left = TreeNode(val, curr.left, None)
                    curr.right = TreeNode(val, None, curr.right)
        return root
