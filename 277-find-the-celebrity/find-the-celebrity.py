# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        
        ## S1: Logical Reduction
        ## T: O(N)
        ## S: O(1)

        x = 0
        for i in range(1, n):
            if knows(x, i):
                x = i
        
        for j in range(n):
            if j != x and (knows(x, j) or not knows(j, x)):
                return -1
        
        return x