class Solution:
    def simplifyPath(self, path: str) -> str:

        ## S1: Stack
        ## T: O(N)
        ## S: O(N)

        stack = []

        for c in path.split("/"):
            if c == ".." and stack:
                stack.pop()
            elif c not in ["", ".", ".."]:
                stack.append(c)
        
        return "/" + "/".join(stack)



        ## S2: Stack
        ## T: O(N)
        ## S: O(N)
        
        stack = []
        arr = [x for x in path.split('/') if x != '.' and x != '']
        
        for c in arr:
            if c == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        
        return '/' + '/'.join(stack)

        