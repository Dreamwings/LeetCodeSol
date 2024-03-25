"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        
        ## S1: Two Pointers
        new = Node(insertVal)

        # Case 1: the linked list is empty
        if head is None:
            new.next = new  # Point the new to itself
            return new
      
        # Initialize two pointers for iterating the linked list
        prev, curr = head, head.next

        # Traverse the linked list
        while curr != head:
            # Case 2: the insert_value should be inserted between prev and curr
            if prev.val <= insertVal <= curr.val:
                break
            
            # Case 3: insertion at the boundary of the largest and smallest values
            if (prev.val > curr.val and (insertVal >= prev.val or insertVal <= curr.val)):
                break  # Correct insertion spot is found

            # Move to the next pair of nodes
            prev, curr = curr, curr.next

        # Case 4: all node values are equal, insert new between prev and curr anywhere
        prev.next = new
        new.next = curr

        # Return the head of the modified linked list
        return head