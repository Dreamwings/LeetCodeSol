class Solution:
    def isValid(self, s: str) -> bool:
        
        ## S1: Stack
        ## T: O(N)
        ## S: O(N)

        if len(s) % 3:
            return False

        stack = []

        for char in s:
            stack.append(char)
            # Check if the last 3 characters in the stack form the string 'abc'
            if ''.join(stack[-3:]) == 'abc':
                # If they do, pop the last 3 characters from the stack
                stack[-3:] = []

        # If the stack is empty after processing the entire string, return True
        # This indicates that the string was composed entirely of 'abc' sequences
        return not stack
