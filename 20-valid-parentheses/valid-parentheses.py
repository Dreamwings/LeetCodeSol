class Solution:
    def isValid(self, s: str) -> bool:
        
        ## S1: Stack

        if not s: return True
        stack = []
        d = {')': '(', ']': '[', '}': '{'}
        
        for c in s:
            if c in '({[':
                stack.append(c)
            else:
                if not stack:
                    return False
                else:
                    x = stack.pop()
                    if d[c] != x:
                        return False
        
        return not stack
        