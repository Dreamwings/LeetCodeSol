"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        from collections import defaultdict, deque

        ## S1: Iterative DFS
        ## T: O(N+M)
        ## S: O(N)
        
        if not node: return None
        
        d = defaultdict(lambda: Node(0, []))
        root = Node(node.val, [])
        d[node.val] = root
        q = [node]
        
        while q:
            x = q.pop()
            xc = d[x.val]
            
            for y in x.neighbors:
                if y.val not in d:
                    q.append(y)
                    d[y.val] = Node(y.val, [])
                
                yc = d[y.val]
                xc.neighbors.append(yc)
        
        return root
        
        """
        ## S2: BFS
        ## T: O(N+M)
        ## S: O(N)

        if not node:
            return node

        # Dictionary to save the visited node and it's respective clone
        # as key and value respectively. This helps to avoid cycles.
        visited = {}

        # Put the first node in the queue
        queue = deque([node])
        # Clone the node and put it in the visited dictionary.
        visited[node] = Node(node.val, [])

        # Start BFS traversal
        while queue:
            # Pop a node say "n" from the from the front of the queue.
            n = queue.popleft()
            # Iterate through all the neighbors of the node
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    # Clone the neighbor and put in the visited, if not present already
                    visited[neighbor] = Node(neighbor.val, [])
                    # Add the newly encountered node to the queue.
                    queue.append(neighbor)
                # Add the clone of the neighbor to the neighbors of the clone node "n".
                visited[n].neighbors.append(visited[neighbor])

        # Return the clone of the node from visited.
        return visited[node]
        """