class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        ## S1: Binary Search

        n = len(numbers)
        nums = numbers
        
        l, r = 0, n - 1
        
        while l < r:
            s = nums[l] + nums[r]
            if s == target:
                return [l+1, r+1]
            elif s > target:
                r -= 1
            else:
                l += 1

        return []