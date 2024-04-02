# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        """
        ## S1: BFS
        ## T: O(N)
        ## S: O(N)

        q = nestedList
        arr = []
        
        while q:
            nxt = []
            x = 0
            for e in q:
                if e.isInteger():
                    x += e.getInteger()
                else:
                    nxt += e.getList()
            arr.append(x)
            q = nxt 
        
        n = len(arr)
        res = 0
        for v in arr:
            res += v * n
            n -= 1
        
        return res
        
        """
        ## S2: DFS (One Pass)
        ## T: O(N)
        ## S: O(N)
        
        max_depth = 1 # can use self.max_depth for global variable
        ans = [] # Add each [int, depth] pair into it

        def dfs(elem, depth=1):
            nonlocal max_depth
            max_depth = max(max_depth, depth)
            if elem.isInteger():
                ans.append([elem.getInteger(), depth])
                return
            for i in elem.getList():
                dfs(i, depth+1)
        
        for elem in nestedList:         
            dfs(elem)        

        return sum(i * (max_depth + 1 - d) for i, d in ans)   

        