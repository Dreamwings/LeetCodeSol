class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ## S1:
        k %= len(nums)
      
        # The last k elements are moved to the front and the remainder are appended
        nums[:] = nums[-k:] + nums[:-k]   
        """

        ## S2:
        n = len(nums)
        k = k % n
        def reverse(nums, i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        reverse(nums, n - k, n - 1)
        reverse(nums, 0, n - k - 1)
        reverse(nums, 0, n - 1)
        
        """

     