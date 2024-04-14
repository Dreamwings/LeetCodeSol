class Solution:
    def calculate(self, s: str) -> int:

        ## S2: No Stack
        ## T: O(N)
        ## S: O(1)

        s += "+"
        pre_op, pre_v, v, res = "+", 0, 0, 0

        for i, c in enumerate(s):
            if c.isdigit():
                v = 10 * v + int(c)
            elif c in "+-*/":
                if pre_op == "+":
                    res += pre_v
                    pre_v = v
                elif pre_op == "-":
                    res += pre_v
                    pre_v = -v
                elif pre_op == "*":
                    pre_v = pre_v * v
                elif pre_op == "/":
                    # if pre_v < 0:
                    #     pre_v = math.ceil(pre_v / v)
                    # else:
                    #     pre_v = pre_v // v
                    pre_v = int(pre_v / v)
                
                v, pre_op = 0, c
        
        return res + pre_v



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

