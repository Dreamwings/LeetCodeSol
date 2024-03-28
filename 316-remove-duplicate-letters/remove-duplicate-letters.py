class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        ## S1: Monotonic Stack
        ## T: O(N)
        ## S: O(N)

        d = {c: i for i, c in enumerate(s)}
        seen = set() # O(1) Space as it's bounded by the number of characters in the alphabet (a constant)
        stack = []
        
        for i, c in enumerate(s):
            if c in seen:
                continue
            while stack and stack[-1] > c and d[stack[-1]] > i:
                seen.remove(stack[-1])
                stack.pop()
            
            stack.append(c)
            seen.add(c)
            # print(seen)
            # print(stack)
        return ''.join(stack)