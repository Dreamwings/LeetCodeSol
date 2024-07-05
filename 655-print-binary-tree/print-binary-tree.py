# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        ## Note there are mistakes in the problem:
        ## 1. m = height
        ## 2. for node at (r, c), its left child is at (r+1, c - 2**(h - r - 2))
        ## and its right child is at (r+1, c + 2**(h - r - 2))

        ## S3: DFS
        ## T: O(N), N is num of nodes
        ## S: O(H * 2^H) ~ O(N^2) since H = N for worst case

        # Helper function to calculate the height of the tree. 
        # The height is the number of edges in the longest path from the root to a leaf.
        def height(node):
            if node is None:
                return 0
            # The height of a node is 1 plus the maximum height of its two children
            return 1 + max(height(node.left), height(node.right))

        # Helper function for the depth-first search that will populate the answer matrix.
        def dfs(node, row, col):
            if node is None:
                return
            
            matrix[row][col] = str(node.val)
            # The offset for placing the next nodes is determined by the height at that level.
            offset = 2 ** (h - row - 2)
            # Recur for left child, updating the row and shifting the column to the left.
            dfs(node.left, row + 1, col - offset)
            # Recur for right child, updating the row and shifting the column to the right.
            dfs(node.right, row + 1, col + offset)

        # Calculate the height of the tree, also the matrix row num
        h = height(root)
        # Calculates the matrix col num
        w = 2 ** h - 1
        
        matrix = [["" for _ in range(w)] for _ in range(h)]
        dfs(root, 0, (w - 1) // 2)
        
        return matrix


        ## S2: DFS
        ## T: O(N), N is num of nodes
        ## S: O(H * 2^H) ~ O(N^2) since H = N for worst case

        def get_height(node):
            if not node: 
                return 0
            return 1 + max(get_height(node.left), get_height(node.right))           
        
        def dfs(node, row, lo, hi):
            # node, node row number, col lower bound, col upper bound
            if not node:
                return
            col = (lo + hi) // 2
            m[row][col] = str(node.val)
            dfs(node.left, row + 1 , lo, col - 1)
            dfs(node.right, row + 1 , col + 1, hi)
            
        h = get_height(root)
        w = 2 ** h - 1
        m = [[''] * w for i in range(h)]
        
        dfs(node=root, row=0, lo=0, hi=w - 1)

        return m
        


        ## S1: BFS
        ## T: O(N), N is num of nodes
        ## S: O(H * 2^H) ~ O(N^2) since H = N for worst case
        
        def height(root):
            if not root: 
                return 0
            return 1 + max(height(root.left), height(root.right))
        
        # if not root: return ['']
        m = height(root)
        n = 2**m - 1
        res = [[''] * n for _ in range(m)]
        
        r, c = 0, (n-1)//2
        q = [(root, c)]
        
        while q:
            nxt = []
            for x, c in q:
                res[r][c] = str(x.val)
                if x.left:
                    nxt.append((x.left, c - 2**(m - r - 2)))
                if x.right:
                    nxt.append((x.right, c + 2**(m - r - 2)))
            r += 1
            q = nxt
        return res

        