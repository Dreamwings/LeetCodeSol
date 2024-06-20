
## S1: DFS
## T: O(N)
## S: O(logN)

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return f"{self.val}"


def stretch_by_k(root, K):

    def helper(node, is_right):
        if not node:
            return

        helper(node.left, False)
        helper(node.right, True)

        node.val //= K

        node_l, node_r = node.left, node.right # Temp nodes to store the original nodes
        node.left, node.right = None, None

        curr = node
        for i in range(K - 1):
            new = TreeNode(node.val)
            if is_right:
                curr.right = new
                curr = curr.right
            else:
                curr.left = new
                curr = curr.left

        curr.left, curr.right = node_l, node_r

    helper(root, False)
    return root


from collections import deque

def print_tree(root):
    q = deque()
    q.append(("root : ", 1, root))

    while q:
        s, level, node = q.popleft()
        print(level, s, node)
        level += 1
        if node.left:
            q.append(("left : ", level, node.left))
        if node.right:
            q.append(("right: ", level, node.right))
        
COUNT = [6]        
def print2DUtil(root, space):
    if root == None:
        return
    # Increase distance between levels
    space += COUNT[0]
    print2DUtil(root.right, space)
    print()
    for i in range(COUNT[0], space):
        print(end=" ")
    print(root.val)
    print2DUtil(root.left, space)

# Example:
root = TreeNode(12)
root.left = TreeNode(81)
root.right = TreeNode(34)

root.left.right = TreeNode(56)
root.right.left = TreeNode(19)
root.right.right = TreeNode(6)

print("\n==================\n")
print_tree(root) 
print2DUtil(root, 0)
print("\n==================\n")
new_root = stretch_by_k(root, 2)
# new_root = stretch_by_k(root, 3)
print_tree(new_root)
print2DUtil(new_root, 0)
print("\n==================\n")

