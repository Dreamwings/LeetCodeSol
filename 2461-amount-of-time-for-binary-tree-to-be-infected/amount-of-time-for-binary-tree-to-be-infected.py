# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        
        from collections import defaultdict, deque

        ## S1: DFS + BFS
        ## T: O(N)
        ## S: O(N)

        # Depth-First Search to build the graph from the binary tree.
        def dfs(node):
            if node is None:
                return
            
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
            
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
            # Recursive call for left and right children.
            dfs(node.left)
            dfs(node.right)

        graph = defaultdict(list)
        dfs(root)
        
        queue = deque([start])
        visited = set() # to keep track of visited nodes.
        time = -1 # ime counter.
        
        while queue:
            # Increase time each level we go deeper in the graph.
            time += 1
            # Traverse nodes at the current level.
            for _ in range(len(queue)):
                x = queue.popleft()
                visited.add(x)
                for y in graph[x]: # check all neighbors of node x
                    if y not in visited:
                        queue.append(y)
        
        return time


        ## S2: One Pass DFS
        ## T: O(N)
        ## S: O(N)

class Solution:
    def __init__(self):
        self.max_distance = 0

    def amountOfTime(self, root, start):
        self.traverse(root, start)
        return self.max_distance

    def traverse(self, root, start):
        depth = 0
        if root is None:
            return depth

        left_depth = self.traverse(root.left, start)
        right_depth = self.traverse(root.right, start)

        if root.val == start:
            self.max_distance = max(left_depth, right_depth)
            depth = -1
        elif left_depth >= 0 and right_depth >= 0:
            depth = max(left_depth, right_depth) + 1
        else:
            distance = abs(left_depth) + abs(right_depth)
            self.max_distance = max(self.max_distance, distance)
            depth = min(left_depth, right_depth) - 1

        return depth