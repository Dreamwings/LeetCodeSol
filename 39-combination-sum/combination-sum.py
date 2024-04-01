class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ## Solution 1: DFS Backtracking
        ##

        a = candidates
        n = len(a)
        
        def dfs(pos, path, target):
            if target < 0: 
                return
            if target == 0:
                res.append(list(path)) # IMPORTANT! res.append(path) will cause error
                return
            
            for i in range(pos, n):
                path.append(a[i])
                dfs(i, path, target - a[i])
                path.pop()
        
        res = []
        dfs(0, [], target)
        return res