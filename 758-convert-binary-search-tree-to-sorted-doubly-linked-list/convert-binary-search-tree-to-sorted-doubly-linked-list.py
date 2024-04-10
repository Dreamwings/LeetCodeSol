"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        ## S1: DFS
        ## T: O(N)
        ## S: O(logN) for avg, O(N) for worst

        if not root:
            return None
        
        def dfs(node):
            # Do recursive traversal of the subtree whose root is "node".
            # Return the head and tail of Doubled Linked List after the subtree is converted
            head = tail = node

            if node.left:
                l_head, l_tail = dfs(node.left)
                l_tail.right = node
                node.left = l_tail
                head = l_head
            
            if node.right:
                r_head, r_tail = dfs(node.right)
                r_head.left = node
                node.right = r_head
                tail = r_tail
            
            head.left, tail.right = tail, head
            
            return head, tail

        return dfs(root)[0]

        """

        ## S2: DFS
        ## T: O(N)
        ## S: O(logN) for avg, O(N) for worst

        def in_order_traverse(node):
            if node is None:
                return
            # Recursive case: traverse the left subtree.
            in_order_traverse(node.left)
          
            # Process the current node.
            nonlocal prev, head
            if prev:
                prev.right = node
                node.left = prev
            else:
                # If this node is the leftmost node
                head = node
            # Mark the current node as the prev one before the next call.
            prev = node
            # Recursive case: traverse the right subtree.
            in_order_traverse(node.right)

        if root is None:
            return None

        head = prev = None
        in_order_traverse(root)
        # Connect the last node visited (prev) with the head.
        prev.right = head
        head.left = prev

        return head
        """