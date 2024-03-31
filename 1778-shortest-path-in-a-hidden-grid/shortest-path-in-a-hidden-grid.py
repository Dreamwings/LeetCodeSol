# """
# This is GridMaster's API interface.
# You should not implement it, or speculate about its implementation
# """
#class GridMaster(object):
#    def canMove(self, direction: str) -> bool:
#        
#
#    def move(self, direction: str) -> bool:
#        
#
#    def isTarget(self) -> None:
#        
#

class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:
        
        ## S1: DFS + BFS
        # Time: O(MN), or 4MN, since we need to check the neighbors for each cell.
        # Space: O(MN)
        
        # DFS for finding the target, also stored the valid cells to be moved
        # It needs to explore the entire map
        # BFS for calculating the distances
        
        can_move = {}
        queue = collections.deque([(0, 0, 0)])
        direction = {'U': (0, 1), 
                     'D': (0, -1), 
                     'L': (-1, 0), 
                     'R': (1, 0)}
        back_dir = {'U': 'D', 
                    'D': 'U', 
                    'L': 'R', 
                    'R': 'L'}
        
        def dfs(x, y):
            nonlocal master
            nonlocal direction
            nonlocal can_move
            nonlocal back_dir
            
            can_move[(x, y)] = master.isTarget()
            
            for d, (dx, dy) in direction.items():
                if (x + dx, y + dy) not in can_move and master.canMove(d):
                    master.move(d)
                    dfs(x + dx, y + dy)
                    master.move(back_dir[d])
        dfs(0, 0)
        
        queue = collections.deque([(0, 0, 0)])
        visited = set()
        
        while queue:
            x, y, d = queue.popleft()
            if can_move[(x, y)] is True:
                return d
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                xx = x + dx
                yy = y + dy
                if (xx, yy) in can_move and (xx, yy) not in visited:
                    visited.add((xx, yy))
                    queue.append((xx, yy, d + 1))
                    
        return -1
