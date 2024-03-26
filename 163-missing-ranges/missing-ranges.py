class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:

        ## S1:

        res = []
        nums = [lower - 1] + nums + [upper + 1]

        for x, y in zip(nums[:-1], nums[1:]):
            if y == x + 2:
                res.append([x + 1, x + 1])
            elif y > x + 2:
                res.append([x + 1, y - 1])

        return res
