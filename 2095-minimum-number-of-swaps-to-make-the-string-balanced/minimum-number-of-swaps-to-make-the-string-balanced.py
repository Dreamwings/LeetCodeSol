class Solution:
    def minSwaps(self, s: str) -> int:
        
        ## S1: Greedy
        ## T: O(N)
        ## S: O(1)

        open_bracket = close_bracket = 0
        for c in s:
            if open_bracket > 0 and c == ']':
                open_bracket -= 1
            elif c == '[':
                open_bracket += 1
            else:
                close_bracket += 1    
        return (open_bracket + 1) // 2