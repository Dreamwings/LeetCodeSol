class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        
        ## S1 DFS Backtracking
        
        def dfs(pos, t, path):
            if t < 0:
                return
            if t == 0:
                res.append(path)
                return
            for i in range(pos, n):
                if i > pos and nums[i] == nums[i-1]:
                    continue
                if nums[i] > t:
                    break
                dfs(i + 1, t - nums[i], path + [nums[i]])
        
        res = []
        nums.sort()  # sort first to check repeated values
        n = len(nums)
        dfs(0, target, [])
        return res
        