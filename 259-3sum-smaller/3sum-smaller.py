class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        
        ## S1: Two Pointers
        ## T: O(N^2)
        ## S: O(1)

        res = 0
        nums.sort()
        n = len(nums)
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] < target:
                    res += right - left
                    left += 1
                else:
                    right -= 1
        return res
