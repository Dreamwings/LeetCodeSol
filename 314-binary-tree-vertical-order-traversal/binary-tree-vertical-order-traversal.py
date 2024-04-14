# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        from collections import defaultdict, deque

        ## S2: BFS, No Sorting
        ## T: O(N)
        ## S: O(N)

        if not root: return []
        d = defaultdict(list)
        q = deque([(root, 0)])
        min_col = max_col = 0

        while q:
            node, col = q.popleft()
            min_col = min(min_col, col)
            max_col = max(max_col, col)
            d[col].append(node.val)

            if node.left:
                q.append((node.left, col - 1))
            if node.right:
                q.append((node.right, col + 1))
        
        return [d[k] for k in range(min_col, max_col + 1)]

        

        ## S1: BFS + Sorting
        ## T: O(NlogN)
        ## S: O(N)
        
        if not root: return []
        d = defaultdict(list)
        q = deque([(root, 0)])
        
        while q:
            node, x = q.popleft()
            d[x].append(node.val)
            if node.left:
                q.append((node.left, x - 1))
            if node.right:
                q.append((node.right, x + 1))
        
        return [d[k] for k in sorted(d)]

        
        ## S3: DFS
        ## T: O(W * HlogH), W is the width, H is the height
        ## S: O(N)

        if root is None:
            return []

        columnTable = defaultdict(list)
        min_column = max_column = 0

        def DFS(node, row, column):
            if node is not None:
                nonlocal min_column, max_column
                columnTable[column].append((row, node.val))
                min_column = min(min_column, column)
                max_column = max(max_column, column)

                # preorder DFS
                DFS(node.left, row + 1, column - 1)
                DFS(node.right, row + 1, column + 1)

        DFS(root, 0, 0)

        # order by column and sort by row
        ret = []
        for col in range(min_column, max_column + 1):
            columnTable[col].sort(key=lambda x:x[0])
            colVals = [val for row, val in columnTable[col]]
            ret.append(colVals)

        return ret