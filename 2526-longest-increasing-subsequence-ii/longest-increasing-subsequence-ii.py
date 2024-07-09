## S1:Segment Tree
## T: build: O(N)
##    modify: O(logN)
##    query: O(logN)
##    totol query O(MlogN), M = len(nums)
## S: O(N)

class Node:
    def __init__(self):
        self.left = 0  # Left boundary of the segment
        self.right = 0  # Right boundary of the segment
        self.value = 0  # The value stored in the node


class SegmentTree:
    def __init__(self, n):
        self.tree = [Node() for _ in range(4 * n)]  # Initialize the segment tree
        self.build(1, 1, n)  # Build the segment tree starting with the root node

    # Build function that initializes each node of the segment tree
    def build(self, node_index, left, right):
        self.tree[node_index].left = left
        self.tree[node_index].right = right
        if left == right:
            # If the left and right boundaries are the same, we're at a leaf node
            return
        mid = (left + right) // 2  # Calculate mid-point to divide the segment
        self.build(node_index * 2, left, mid)  # Initialize left child
        self.build(node_index * 2 + 1, mid + 1, right)  # Initialize right child

    # Modify the value of a single element and update the tree accordingly
    def modify(self, node_index, index, value):
        if self.tree[node_index].left == index and self.tree[node_index].right == index:
            # If the current node corresponds to the element index, update its value
            self.tree[node_index].value = value
            return
        mid = (self.tree[node_index].left + self.tree[node_index].right) // 2
        if index <= mid:
            self.modify(node_index * 2, index, value)  # Modify left child
        else:
            self.modify(node_index * 2 + 1, index, value)  # Modify right child
        self.push_up(node_index)  # Update the current node's value based on its children

    # Push up the changes from children to the parent node
    def push_up(self, node_index):
        self.tree[node_index].value = max(self.tree[node_index * 2].value, self.tree[node_index * 2 + 1].value)

    # Query the maximum value in the given range [l, r]
    def query(self, node_index, left, right):
        if self.tree[node_index].left >= left and self.tree[node_index].right <= right:
            # If the current segment is entirely within the query range, return its value
            return self.tree[node_index].value
        mid = (self.tree[node_index].left + self.tree[node_index].right) // 2
        max_value = 0
        if left <= mid:
            max_value = self.query(node_index * 2, left, right)  # Query left child
        if right > mid:
            # Query right child and keep the maximum value found
            max_value = max(max_value, self.query(node_index * 2 + 1, left, right))
        return max_value


class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        
        # Initialize the segment tree with the maximum value in nums as its size
        tree = SegmentTree(max(nums))
        max_length = 1
        for value in nums:
            # Query the longest increasing subsequence ending before value within the range [value-k, value-1]
            length = tree.query(1, value - k, value - 1) + 1
            max_length = max(max_length, length)  # Update the maximum LIS length
            tree.modify(1, value, length)  # Update the tree with the new LIS ending at value
        return max_length  # Return the maximum length of LIS found
        

