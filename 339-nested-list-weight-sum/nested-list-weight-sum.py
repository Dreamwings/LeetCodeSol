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
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        
        ## S1: Iterative BFS
        ## T: O(N)
        ## S: O(N)

        w = 1
        res = 0
        
        while nestedList:
            nxt = []
            for e in nestedList:
                if e.isInteger():
                    res += e.getInteger() * w
                else:
                    nxt += e.getList()
            w += 1
            nestedList = nxt
        
        return res
        
        

        ## S2: Recursive DFS
        ## T: O(N)
        ## S: O(D), D is max depth

        def dfs(nested_list, depth): 
            summ = 0 # initialization of the summ
            for x in nested_list:
                # if the element is integer
                if x.isInteger():
                    summ += x.getInteger() * depth # multiply by the depth
                # if the element is List    
                else:
                    summ += dfs(x.getList(), depth+1) # increment the depth by 1        
            return summ
    
        return dfs(nestedList, 1)   # start with depth=1
        