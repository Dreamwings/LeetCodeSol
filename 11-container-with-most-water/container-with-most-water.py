class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        
        ## S2: Two Pointers
        ## T: O(N)
        ## S: O(1)
        
        n = len(height)
        l, r = 0, n - 1
        res = 0
        
        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return res      

        """
        ## S1: Brute Force

        maxarea = 0
        for left in range(len(height)):
            for right in range(left + 1, len(height)):
                width = right - left
                maxarea = max(maxarea, min(height[left], height[right]) * width)

        return maxarea
        """