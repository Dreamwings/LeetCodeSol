class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        ## S1: Stack
        
        stack = []
        
        for x in asteroids:
            if x > 0:
                stack.append(x)
            else:
                while stack and stack[-1] > 0 and stack[-1] < -x:
                    stack.pop()
                
                if stack and stack[-1] + x == 0:
                    stack.pop()
                    continue
                if not stack or stack[-1] < 0:
                    stack.append(x)
        
        return stack
        