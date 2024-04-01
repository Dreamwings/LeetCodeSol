class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        ## S1: Monotonic Stack
        ## T: O(N)
        ## S: O(N)
        
        n = len(temperatures)
        res = [0] * n
        stack = []
        
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                j = stack.pop()
                res[j] = i - j
            
            stack.append(i)
        
        return res