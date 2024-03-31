class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        from collections import deque

        ## S1: BFS

        # the offsets in the eight directions
        offsets = [(1, 2), (2, 1), (2, -1), (1, -2),
                   (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

        q = deque()
        q.append((0, 0))
        visited = {(0, 0)}
        steps = 0

        while q:
            for _ in range(len(q)):
                xx, yy = q.popleft()
                if (xx, yy) == (x, y):
                    return steps
                
                for dx, dy in offsets:
                    i, j = xx + dx, yy + dy
                    if (i, j) not in visited:
                        q.append((i, j))
                        visited.add((i, j))
            steps += 1

        return -1