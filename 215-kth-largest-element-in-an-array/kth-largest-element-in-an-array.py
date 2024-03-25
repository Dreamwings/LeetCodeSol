class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        from heapq import nlargest, heappush, heappop


        ## S3: Quick Select (Recursive)
        ## Time: O(N) for best and avg, O(N^2) for worst
        ## Space: O(N)

        if not nums: return
        p = random.choice(nums) # pivot

        gt, eq, st = [], [], []
        for x in nums:
            if x > p:
                gt.append(x)
            elif x == p:
                eq.append(x)
            else:
                st.append(x)
    
        GL, EL = len(gt), len(eq)
        if k <= GL:
            return self.findKthLargest(gt, k)
        elif k <= GL + EL:
            return p
        else:
            return self.findKthLargest(st, k - GL - EL)
            

        """
        ## Solution 1:
        ## Time: O(NlogK)
        return nlargest(k, nums)[-1]
        
        
        ## Solution 2:
        ## Time: O(NlogK)
        q = []

        for x in nums:
            heappush(q, x)
            if len(q) > k:
                heappop(q)

        return q[0]
        
        ## S5: Counting Sort
        ## https://leetcode.com/problems/kth-largest-element-in-an-array/solutions/4760057/counting-sort-easy-and-optimised-python/


        ## S4: Quick Select (Iterative)
        ## Time: O(N) for best and avg, O(N^2) for worst
        ## Space: O(N)
        ## Time Limit Exceeded

        def partition(left, right, pivot_index):
            pivot = nums[pivot_index]
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            index = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[index], nums[i] = nums[i], nums[index]
                    index += 1
            nums[right], nums[index] = nums[index], nums[right]
            return index 
        
        def quick_select(left = 0, right = len(nums)-1):
            if left > right: return 
            pivot_index = random.randint(left, right)
            index = partition(left, right, pivot_index)
            if index == n_smaller: return 
            elif index > n_smaller: quick_select(left, index-1)
            else: quick_select(index+1, right)
        
        n_smaller = len(nums)-k
        quick_select()
        return nums[n_smaller]
        """