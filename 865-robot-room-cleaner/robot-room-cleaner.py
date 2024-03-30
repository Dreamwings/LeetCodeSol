# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        
        ## S1: DFS Backtracking
        ## T: O(4^(N-M))
        ## S:  O(N)

        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        k = 0
        visited = set()
        
        def goBack(r):
            r.turnLeft()
            r.turnLeft()
            r.move()
            r.turnRight()
            r.turnRight()
        
        def dfs(r, k, i, j, visited):
            r.clean()
            visited.add((i, j))
            
            for _ in range(4):
                x = i + d[k][0]
                y = j + d[k][1]
                if (x, y) not in visited and r.move():
                    dfs(r, k, x, y, visited)
                    goBack(r)
                r.turnRight()
                k = (k + 1) % 4
                
        dfs(robot, k, 0, 0, visited)


        