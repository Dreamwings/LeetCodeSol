class Solution:
    import random

    ## S1:
    ## T: O(N)
    ## S: O(N)

    def __init__(self, nums: List[int]):
        # Store the original list of numbers
        self.nums = nums
        # Make a copy of the original list to keep it intact for reset purposes
        self.original = nums.copy()

    def reset(self) -> List[int]:
        # Reset the nums list to the original configuration
        self.nums = self.original.copy()
        # Return the reset list
        return self.nums

    def shuffle(self) -> List[int]:
        # Shuffle the list of numbers in-place using the Fisher-Yates algorithm
        for i in range(len(self.nums)):
            # Pick a random index from i (inclusive) to the end of the list (exclusive)
            j = random.randrange(i, len(self.nums))
            # Swap the current element with the randomly chosen one
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        # Return the shuffled list
        return self.nums
        
    """
    ## S2:

    def __init__(self, nums: List[int]):
        # Store the original list of numbers
        self.d = nums[:]

    def reset(self) -> List[int]:
        return self.d

    def shuffle(self) -> List[int]:
        ## Approach 1: faster        
        arr = self.d[:]
        random.shuffle(arr)
        return arr
        
        '''
        ## Approach 2:        
        return sorted(self.d, key=lambda x: random.random())
        '''
    """    


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()