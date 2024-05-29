class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:

        ## S3: BFS
        ## https://leetcode.com/problems/remove-invalid-parentheses/solutions/75028/short-python-bfs/
        ## T: O(N * 2^N), 2^N possible subsets of brakets, each need O(N) for isvalid check.
        ## S: O(2^N) for worst case

        # The idea is to remove 1 single char at each position of s for each level/step. 
        # When there are valid str at a level, add them all to the res array and return
        # 1st level: s
        # 2nd level: all subsequences by removing 1 ch from s
        # 3rd level: all subsequences by removing 2 ch from s
        # ...

        def isvalid(s):
            cnt = 0
            for c in s:
                cnt += (c == '(') - (c == ')')
                if cnt < 0:
                    return False
            return cnt == 0

        q = {s} # Here must use set() because for deeper levels there might be duplicated strings
        while q:
            res = list(filter(isvalid, q))
            if res:
                return res
            q = {s[:i] + s[i+1:] for s in q for i in range(len(s))}


        ## S4: BFS

        def isvalid(s):
            s = ''.join(filter('()'.count, s))
            while '()' in s:
                s = s.replace('()', '')
            return not s

        level = {s}
        while True:
            valid = list(filter(isvalid, level))
            if valid:
                return valid
            level = {s[:i] + s[i+1:] for s in level for i in range(len(s))} 



        ## S2: DFS (24ms)
        ## T: O(2^N)
        ## S: O(N) to O(2^N) for worst case
        
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


        
        ## S1: DFS Backtracking  (32ms)
        ## T: O(2^N)
        ## S: O(N + |res|), worst case O(2^N)
        
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
        
      