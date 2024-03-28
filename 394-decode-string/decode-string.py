class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        ## S1: Stack (Single Stack)
        ## T: O(N)
        ## S: O(N)
        
        stack = []
        v, res = 0, ''
        letters = 'abcdefghijklmnopqrstuvwxyz'
        
        for c in s:
            if c.isdigit():
                v = v * 10 + int(c)
            elif c in letters:
                res += c
            elif c == '[':
                stack.append(res)
                stack.append(v)
                v, res = 0, ''
            elif c == ']':
                pre_v = stack.pop()
                pre_res = stack.pop()
                res = pre_res + res * pre_v
        
        return res

        """
        ## S2: Two Stacks
        ## T: O(N)
        ## S: O(N)

        nums = []
        strs = []
        num = ""
        s = ""
        for i, ch in enumerate(string):
            if ch.isdigit():
                num += ch
            elif ch == "[":
                nums.append(int(num))
                strs.append(s)
                num = ""
                s = ""
            elif ch == "]":
                s =  strs.pop() + nums.pop() * s        # watchout, replacing with the same string
            else:
                s += ch
        return s


        ## S3: Recursive DFS  

        def decode(idx=0):
            '''decode the string and return the last decoded idx'''
            subs = []
            curnum = 0
            while idx < len(s):
                if s[idx].isdigit(): curnum = curnum * 10 + int(s[idx])
                elif s[idx] == '[':
                    decsub, idx = decode(idx + 1)
                    subs.append(max(curnum, 1) * decsub)
                    curnum = 0
                elif s[idx] == ']': break
                else: subs.append(s[idx])
                idx += 1
            return ''.join(subs), idx
            
        return decode()[0]
        """      