class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        ## S1: Three Pointers
        ## T: O(N)
        ## S: O(1)

        # Three variables to store maxiumum three numbers till now.
        first_max = -inf
        second_max = -inf
        third_max = -inf
    
        for num in nums:
            # This number is already used once, thus we skip it.
            if first_max == num or second_max == num or third_max == num:
                continue
            
            # If current number is greater than first maximum,
            # It means that this is the greatest number and first maximum and second max
            # will become the next two greater numbers.
            if first_max <= num:
                third_max = second_max
                second_max = first_max
                first_max = num
            # When current number is greater than second maximum,
            # it means that this is the second greatest number.
            elif second_max <= num:
                third_max = second_max
                second_max = num
            # It is the third greatest number.
            elif third_max <= num:
                third_max = num
        
        # If third max was never updated, it means we don't have 3 distinct numbers.
        if third_max == -inf:
            return first_max
        
        return third_max

        """
        ## S2: Min Heap
        ## T: O(N)
        ## S: O(1)

        min_heap = []
        taken = set()
        
        for index in range(len(nums)):
            # If current number was already taken, skip it.
            if nums[index] in taken:
                continue
            
            # If min heap already has three numbers in it.
            # Pop the smallest if current number is bigger than it.
            if len(min_heap) == 3:
                if min_heap[0] < nums[index]:
                    taken.remove(min_heap[0])
                    heappop(min_heap)
                    
                    heappush(min_heap, nums[index])
                    taken.add(nums[index])
                    
            # If min heap does not have three numbers we can push it.
            else:
                heappush(min_heap, nums[index])
                taken.add(nums[index])
        
        # 'nums' has only one distinct element it will be the maximum.
        if len(min_heap) == 1:
            return min_heap[0]
        
        # 'nums' has two distinct elements.
        elif len(min_heap) == 2:
            first_num = min_heap[0]
            heappop(min_heap)
            return max(first_num, min_heap[0])
        
        return min_heap[0]


        ## S3: Ordered Set
        ## T: O(N)
        ## S: O(1)
        from sortedcontainers import SortedSet

        sorted_nums = SortedSet()
        
        # Iterate on all elements of 'nums' array.
        for num in nums:
            # Do not insert same element again.
            if num in sorted_nums:
                continue
            
            # If sorted set has 3 elements.
            if len(sorted_nums)== 3:
                # And the smallest element is smaller than current element.
                if sorted_nums[0] < num:
                    # Then remove the smallest element and push the current element.
                    sorted_nums.discard(sorted_nums[0])
                    sorted_nums.add(num)
            # Otherwise push the current element of nums array.
            else:
                sorted_nums.add(num)
        
        # If sorted set has three elements return the smallest among those 3.
        if len(sorted_nums) == 3:
            return sorted_nums[0]
        
        # Otherwise return the biggest element of nums array.
        return sorted_nums[-1]

        
        ## S4: Sorting
        ## T: O(NlogN)
        """