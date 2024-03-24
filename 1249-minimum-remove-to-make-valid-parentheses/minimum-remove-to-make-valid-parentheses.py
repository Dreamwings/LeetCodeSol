class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        ## S3: Stack
        ## T: O(N)
        ## S: O(N)

        s = list(s)
        stack = []
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    s[i] = ''
        
        while stack:
            s[stack.pop()] = ''

        return ''.join(s)
        
        """
        ## S1: Stack
        ## T: O(N)
        ## S: O(N)

        cur, stack = "", []

        for c in s:
            if c == "(":
                stack.append(cur)
                cur = ""
            elif c == ")":
                if stack:
                    cur = stack.pop() + "(" + cur + ")"
            else:
                cur += c
        
        return "".join(stack) + cur

        ## S2:
        ## Time: O(3N)
        ## Space: O(N)
        cnt = 0
        h = set()
        n = len(s)
        
        for i, c in enumerate(s):
            if c == '(':
                cnt += 1
            if c == ')':
                cnt -= 1
            if cnt < 0:
                h.add(i)
                cnt = 0
        cnt = 0
        for i, c in enumerate(s[::-1]):
            if c == ')':
                cnt += 1
            if c == '(':
                cnt -= 1
            if cnt < 0:
                h.add(n-1-i)
                cnt = 0
        
        res = ''
        for i, c in enumerate(s):
            if i in h:
                continue
            res += c
        
        return res
        """
        