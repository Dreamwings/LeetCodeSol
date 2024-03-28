class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:


        smallest = float('inf')
        middle = float('inf')

        for num in nums:
            if num > middle:
            # an increasing triplet exists.
                return True
            if num <= smallest:
            # update the smallest number to be the current number.
                smallest = num
            else:
                middle = num

        return False
