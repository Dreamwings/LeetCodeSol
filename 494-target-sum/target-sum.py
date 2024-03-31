class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        from collections import defaultdict
        
        ## S 2: BFS
        ## Special level traversal BFS
        
        cnt = defaultdict(int)  # target value: number of expressions
        cnt[0] = 1
        
        for x in nums:
            new = defaultdict(int)
            for y, v in cnt.items():
                new[y + x] += v
                new[y - x] += v
            cnt = new
        
        return cnt[target]
        