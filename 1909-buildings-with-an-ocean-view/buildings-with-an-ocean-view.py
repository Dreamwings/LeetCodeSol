class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:

        ## S1: 
        ## T: O(N)
        ## S: O(1)

        res,  max_height = [], 0

        # From right to left
        for i in range(len(heights) - 1, -1, -1):
            # Compare the current height with the max height found so far
            if heights[i] > max_height:
                res.append(i)
                max_height = heights[i]
      
        return res[::-1] # The resulting list is in reverse order

        """
        ## S2: Stack
        ## T: O(N)
        ## S: O(N)

        res = []

        for i in range(len(heights)):
            # 如果当前高度大于之前的 必须把之前的都退出来
            while res and heights[res[-1]] <= heights[i]:
                res.pop(-1)
            res.append(i)
        
        return res
        """
