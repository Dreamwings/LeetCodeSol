class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        ## S1: Greedy and Two Pointers
        ## T: O(N)
        ## S: O(1)
    
        res = 0
        l, r = 0, len(nums) - 1
        left_sum, right_sum = nums[0], nums[-1]

        while l < r:
            if left_sum < right_sum:
                l += 1
                left_sum += nums[l]
                res += 1
            elif left_sum > right_sum:
                r -= 1
                right_sum += nums[r]
                res += 1
            else:  # left_sum == right_sum
                l += 1
                r -= 1
                left_sum = nums[l]
                right_sum = nums[r]

        return res
