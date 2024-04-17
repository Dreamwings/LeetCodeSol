class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:

        ## S3:
        ## T: O(N)
        ## S: O(1)

        res=[]
        nums.append(upper + 1)  # O(1)

        for x in nums:
            if x > lower:
                res.append([lower, x - 1])
            lower = x + 1

        return res



        ## S2: 

        res = []
        nums = [lower - 1] + nums + [upper + 1]

        for x, y in zip(nums[:-1], nums[1:]):
            lo = x + 1
            hi = y - 1
            if lo <= hi:
                res.append([lo, hi])
        
        return res

        
        ## S1:

        res = []
        nums = [lower - 1] + nums + [upper + 1]

        for x, y in zip(nums[:-1], nums[1:]):
            if y == x + 2:
                res.append([x + 1, x + 1])
            elif y > x + 2:
                res.append([x + 1, y - 1])

        return res
