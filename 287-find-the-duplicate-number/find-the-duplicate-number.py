class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        ## S6: Negative Marking
        ## Time: O(N)
        ## Space: O(1)

        for num in nums:
            cur = abs(num)
            if nums[cur] < 0:
                duplicate = cur
                break
            nums[cur] = -nums[cur]

        # Restore numbers
        for i in range(len(nums)):
            nums[i] = abs(nums[i])

        return duplicate


        """

        ## S5: Linked List Cycle (LC 142)
        ## Time: O(N)
        ## Space: O(1)
        
        fast = slow = nums[0]
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            # print(slow, fast)
            if slow == fast:
                break
        
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            
        return slow
        
        
        ## S4: Set
        ## Time: O(N)
        ## Space: O(N)

        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)


        ## S3: Bit Operation
        ## Time: O(N)
        ## Space: O(N)
        ## But it can be very slow with bit operation if n is very large
        
        mask = 0
        
        for x in nums:
            cur = 1 << x
            if mask & cur:
                return x
            mask |= cur
            
        
        ## S1: Sorting
        ## Time: O(NlogN)
        ## Space: O(1)

        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]

        
        ## S2: Binary Search
        ## Time: O(NlogN)
        ## Space: O(1)
        
        lo, hi = 1, len(nums) - 1
        
        while lo < hi:
            m = (lo + hi) // 2
            cnt = 0
            for x in nums:
                if x <= m:
                    cnt += 1
            
            if cnt > m:  
                # the number of x smaller or equal than m (1 to m) is more than m
                # which means the repeated num is on the left half, in [1, m] inclusive
                hi = m
            else: # the repeated num is on the right half
                lo = m + 1
        
        return lo
        """
