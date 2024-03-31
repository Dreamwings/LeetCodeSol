class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        ## S1: Hash Map and Presum
        
        n = len(nums)
        d = {0: -1}
        cnt = res = 0
        
        for i, x in enumerate(nums):
            cnt += [-1, 1][x == 1]  # x: 1, cnt += 1; 0, cnt -= 1
            # cnt is the number difference between 1 and 0
            # if we find the same value of cnt previously at j, it means:
            # nums[:j+1] and nums[:i+1] has the same cnt value
            # then nums[j+1:i+1] has the same numbers of 1 and 0
            if cnt in d:
                j = d[cnt]
                res = max(res, i - j)
            else:
                d[cnt] = i
        return res