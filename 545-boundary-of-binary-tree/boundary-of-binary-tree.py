# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        
        ## S3: DFS
        ## T: O(N)
        ## S: O(N)

        # The main idea is to carry the flag isleft and isight
        # in the dfs steps to help decide when to add node
        # values to the boundary array.
        if not root: return []
        boundary = [root.val]
        def dfs(root, isleft, isright):
            if root:
                # append when going down from the left or at leaf node
                if (not root.left and not root.right) or isleft:
                    boundary.append(root.val)
                
                if root.left and root.right:
                    dfs(root.left, isleft, False)
                    dfs(root.right, False, isright)
                else:
                    dfs(root.left,  isleft, isright)
                    dfs(root.right, isleft, isright)
                
                # append to boundary when coming up from the right
                if (root.left or root.right) and isright:
                    boundary.append(root.val)
        
        dfs(root.left, True, False)
        dfs(root.right, False, True)
        return boundary


        """
        ## S1: DFS
        ## T: O(N)
        ## S: O(N)

        def dfs_leftmost(node):
            if not node or not node.left and not node.right:
                return
            boundary.append(node.val)
            if node.left:
                dfs_leftmost(node.left)
            else:
                dfs_leftmost(node.right)

        def dfs_leaves(node):
            if not node:
                return
            dfs_leaves(node.left)
            if node != root and not node.left and not node.right:
                boundary.append(node.val)
            dfs_leaves(node.right)

        def dfs_rightmost(node):
            if not node or not node.left and not node.right:
                return
            if node.right:
                dfs_rightmost(node.right)
            else:
                dfs_rightmost(node.left)
            boundary.append(node.val)

        if not root:
            return []
        boundary = [root.val]
        dfs_leftmost(root.left)
        dfs_leaves(root)
        dfs_rightmost(root.right)
        return boundary



        ## S2: DFS
        ## AlgoMonster
        """