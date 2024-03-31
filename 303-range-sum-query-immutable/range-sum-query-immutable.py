## S2:

from itertools import accumulate

class NumArray:
    def __init__(self, nums: List[int]):
        # Pre-calculate the cumulative sum of the array.
        # The 'initial=0' makes sure the sum starts from index 0 for easier calculations.
        self.cumulative_sum = list(accumulate(nums, initial=0))

    def sumRange(self, left: int, right: int) -> int:
        # Calculate the sum of elements between 'left' and 'right'
        # by subtracting the sum up to 'left' from the sum up to 'right + 1'.
        return self.cumulative_sum[right + 1] - self.cumulative_sum[left]


"""
## S1:

class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.s = [0] * n
        self.s[0] = nums[0]
        for i in range(1, n):
            self.s[i] = self.s[i-1] + nums[i]
        

    def sumRange(self, left: int, right: int) -> int:

        if left == 0: return self.s[right]
        return self.s[right] - self.s[left-1]
"""


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)