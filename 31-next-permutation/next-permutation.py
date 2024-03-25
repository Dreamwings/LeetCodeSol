class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        ## S1: 
        ## use the example :[1,2,3,4,5,5,5,4,3,2,1]
        ## how ?     step 1:[1,2,3,5,5,5,4,4,3,2,1] from swap nums[3] = 4 and nums[6] = 5
        ##           step 2:[1,2,3,5] + list(reversed([5,5,4,4,3,2,1]]))
        ## next permutation:[1,2,3,5,1,2,3,4,4,5,5]
        
        
        n = len(nums)
        i = j = n - 1
        
        while i and nums[i-1] >= nums[i]:
            i -= 1
        
        if i == 0:  # the array is non-increasing
            nums.reverse()
            return
        
        k = i - 1
        while nums[j] <= nums[k]:
            j -= 1
            
        nums[k], nums[j] = nums[j], nums[k]
        
        l, r = k + 1, n - 1
        # while l < r:
        #     nums[l], nums[r] = nums[r], nums[l]
        #     l += 1
        #     r -= 1
        nums[l:] = nums[l:][::-1]
        
        """

        ## S2:

        n = len(nums)
      
        # First, find the first element from the right that is smaller than the element next to it.
        pivot = -1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot = i
                break
      
        # If such an element was found, then we can form the next permutation
        if pivot != -1:
            # Now, we find the smallest element greater than the 'pivot', starting from the end
            for j in range(n - 1, pivot, -1):
                if nums[j] > nums[pivot]:
                    # Swap the 'pivot' with this element
                    nums[pivot], nums[j] = nums[j], nums[pivot]
                    break
      
        # Finally, reverse the elements following the 'pivot' (inclusive if pivot is -1)
        # to get the lowest possible sequence with the 'pivot' being the prefix
        nums[pivot + 1:] = reversed(nums[pivot + 1:])
        """