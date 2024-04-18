# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## S1: Deque
## T: O(N) for constructor, O(1) for next and hasNext
## S: O(N)

class BSTIterator:
    
    from collections import deque
    
    def __init__(self, root: Optional[TreeNode]):
        self.d = deque()
        self.inorder(root)
    
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            self.d.append(node.val)
            self.inorder(node.right)

    def next(self) -> int:
        if self.hasNext:
            return self.d.popleft()        

    def hasNext(self) -> bool:
        return len(self.d) > 0
        
## S2: Pointers
## T: O(N) for constructor, O(1) for next and hasNext
## S: O(N)

class BSTIterator:

    def __init__(self, root: TreeNode):

        self.nodes_sorted = []
        # Pointer to the next smallest element in the BST
        self.index = -1
        # Call to flatten the input binary search tree
        self._inorder(root)

    def _inorder(self, root):
        if not root:
            return
        self._inorder(root.left)
        self.nodes_sorted.append(root.val)
        self._inorder(root.right)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        self.index += 1
        return self.nodes_sorted[self.index]

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.index + 1 < len(self.nodes_sorted)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()