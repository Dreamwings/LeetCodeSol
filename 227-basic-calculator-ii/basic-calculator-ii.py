class Solution:
    def calculate(self, s: str) -> int:
        
        ## S1: Stack
        ## T: O(N)
        ## S: O(N)
        
        s += "+"
        pre_op, v, stack = "+", 0, []
        
        for c in s:
            if c.isdigit():
                v = 10 * v + int(c)
            elif c in "+-*/":
                if pre_op == "+":
                    stack.append(v)
                elif pre_op == "-":
                    stack.append(-v)
                elif pre_op == "*":
                    x = stack.pop()
                    stack.append(x * v)
                elif pre_op == "/":
                    x = stack.pop()
                    stack.append(int(x/v))
                
                v, pre_op = 0, c
        
        return sum(stack)

