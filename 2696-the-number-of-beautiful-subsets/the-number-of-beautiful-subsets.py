class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        
        ## S1: Iterative Backtracking
        ## T: 

        q = deque( [([], -1)] )
        res = 0
        
        while q:
            cur, idx = q.popleft()
            res += 1
            
            for i in range(idx + 1, len(nums)):
                if nums[i] - k in cur or nums[i] + k in cur:
                    continue
                q.append( (cur + [nums[i]], i) )
        
        return res - 1

        """
        ## S2: Recursive DFS Backtracking

        def depth_first_search(index: int) -> None:
            nonlocal beautiful_count 
            # Base case: check if we have considered all numbers.
            if index >= len(nums):
                beautiful_count += 1 # Found a beautiful subset.
                return
          
            # Recursive case 1: Skip the current number and move to the next.
            depth_first_search(index + 1)
          
            # Recursive case 2: Include the current number if it can form a beautiful subset.
            if count[nums[index] + k] == 0 and count[nums[index] - k] == 0:
                count[nums[index]] += 1 # Include the current number in the count.
                depth_first_search(index + 1) # Move to the next number.
                count[nums[index]] -= 1 # Backtrack by removing the current number from the count.

        # Initialize the answer to -1 to account for the empty subset which is not considered beautiful.
        beautiful_count = -1
        count = Counter() # Counter to track the occurrences of numbers in the current subset.
      
        # Begin the depth-first search with the first number in the list.
        depth_first_search(0)
      
        return beautiful_count

        
        ## S3: DP
        ## T: O(NlogN + K)
        ## S: O(N + K)

        count = [Counter() for i in range(k)]
        for a in A:
            count[a % k][a] += 1
        res = 1
        for i in range(k):
            prev, dp0, dp1 = 0, 1, 0
            for a in sorted(count[i]):
                v = pow(2, count[i][a])
                if prev + k == a:
                    dp0, dp1 = dp0 + dp1, dp0 * (v - 1)
                else:
                    dp0, dp1 = dp0 + dp1, (dp0 + dp1) * (v - 1)
                prev = a
            res *= dp0 + dp1
        return res - 1

        """