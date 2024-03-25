class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        ## Solutionn 1: DFS (24ms)
        ## T: O(2^N) < T < O(3^N)
        ## S: O(N)
        
        def dfs(s, lo, hi, res, d = {'(': 1, ')': -1}):
            cnt = 0
            for i in range(hi, len(s)):
                if s[i] in d:
                    cnt += d[s[i]]
                if cnt < 0:
                    for j in range(lo, i+1):
                        if s[j] not in d:  # s[j] is a letter, not '(' or ')'
                            continue
                        if j > lo and s[j] == s[j-1]: # two consecutive chr are the same
                            continue
                        if d[s[j]] == -1:
                            s_new = s[:j] + s[j+1:]
                            dfs(s_new, j, i, res, d)
                    return
                
            s_rev = s[::-1]
            if d[')'] == -1:
                dfs(s_rev, 0, 0, res, d = {'(': -1, ')': 1})
            else:
                res.append(s_rev)
        
        
        res = []
        dfs(s, 0, 0, res, d = {'(': 1, ')': -1})
        return res

        """
        
        ## S2: DFS Backtracking  (32ms)
        
        def valid(x):  # to check if a string x is valid
            l_minus_r = 0
            for c in x:
                if c == '(': l_minus_r += 1
                elif c == ')': l_minus_r -= 1
                if l_minus_r < 0: return False
            
            return l_minus_r == 0
        
        def dfs(ss, pos, l_rem, r_rem):
            if l_rem == 0 and r_rem == 0:
                if valid(ss):
                    res.append(ss)
                return
            
            # first get the final len of ss after remove all invalid chr
            new_len = len(ss) - l_rem - r_rem
            
            for i in range(pos, new_len + 1):
                # consider if two neighbors are the same chr, it cause duplicates in final result
                if i > pos and ss[i] == ss[i-1]:
                    continue
                if ss[i] not in '()':  # not parentheses, but letters
                    continue
                s_new = ss[:i] + ss[i+1:]  # remove ss[i], which is '(' or ')'
                if ss[i] == '(' and l_rem > 0:
                    dfs(s_new, i, l_rem - 1, r_rem)
                if ss[i] == ')' and r_rem > 0:
                    dfs(s_new, i, l_rem, r_rem - 1)
            
            
        # first calculate how many left to remove and how many right to remove
        l_rem, r_rem = 0, 0
        for c in s:
            if c == '(':
                l_rem += 1
            elif c == ')':
                if l_rem > 0:
                    l_rem -= 1
                else:
                    r_rem += 1
        
        res, n = [], len(s)
        if l_rem + r_rem == n:  # means need to remove all chr in s
            return ['']
        
        dfs(s, 0, l_rem, r_rem)
        return res
        
        
        """
        