class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        ## use the example :[1,2,3,4,5,5,5,4,3,2,1]
        ## how ?     step 1:[1,2,3,5,5,5,4,4,3,2,1] from swap nums[3] = 4 and nums[6] = 5
        ##           step 2:[1,2,3,5] + list(reversed([5,5,4,4,3,2,1]]))
        ## next permutation:[1,2,3,5,1,2,3,4,4,5,5]


        ## S2:
        ## T: O(N)
        ## S: O(1)

        n = len(nums)
        i = j = n - 1

        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1

        # if i == 0, the array is non-increasing, go to the last step to reverse it directly
        if i > 0:
            while nums[j] <= nums[i - 1]:
                j -= 1
            nums[j], nums[i - 1] = nums[i - 1], nums[j]

        nums[i:]= reversed(nums[i:])


        """
        ## S1: 
        ## T: O(N)
        ## S: O(1)
        
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
        nums[l:] = nums[l:][::-1] # Reverse this part
        
        """
