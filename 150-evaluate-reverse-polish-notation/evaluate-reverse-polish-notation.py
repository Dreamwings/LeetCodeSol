class Solution(object):
    def evalRPN(self, tokens: List[str]) -> int:
        
        ## S1: Stack
        ## T: O(N)
        ## S: O(N)

        stack = []
        ops = {"+": lambda x, y: x + y,
               "-": lambda x, y: x - y,
               "*": lambda x, y: x * y,
               "/": lambda x, y: int(x / y),
               }

        for e in tokens:
            if e in ops:
                y = stack.pop()
                x = stack.pop()
                op = ops[e]
                stack.append(op(x, y))
            else:
                stack.append(int(e))
        
        return stack.pop()
        


        ## S2: Stack
        ## T: O(N)
        ## S: O(N)

        stack = []

        for e in tokens:
            if e in "+-*/":
                y, x = stack.pop(), stack.pop()
                if e == "+":
                    stack.append(x + y)
                elif e == "-":
                    stack.append(x - y)
                elif e == "*":
                    stack.append(x * y)
                else:
                    stack.append(int(x / y))
            else:
                stack.append(int(e))
        
        return stack.pop()