class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        from heapq import nlargest, heappush, heappop
        
        ## S3: Quick Select (Recursive)
        ## Time: O(N) for best and avg, O(N^2) for worst
        ## Space: O(N)
        ## By using the median of medians algorithm, we can improve to a worst-case 
        ## scenario time complexity of O(n).

        if not nums: return
        p = random.choice(nums) # pivot
        gt, eq, st = [], [], [] # elem > p, elem == p, elem < p

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
            

        
        ## S1: Heap nlargest
        ## Time: O(NlogK)
        ## Space: O(N)
        
        return nlargest(k, nums)[-1]
        
        
        ## S2: Min Heap
        ## Time: O(NlogK)
        ## Space: O(N)

        q = []

        for x in nums:
            heappush(q, x)
            if len(q) > k:
                heappop(q)

        return q[0]



        ## S5: Counting Sort
        ## T: O(N + M), N = len(nums), M = max_v - min_v + 1
        ## S: O(M)
        ## Counting Sort may not be good for this question as M can be much larger than N
        ## But if the question is K-th Most Frequent element in an array, Counting Sort
        ## is even better than Quick Select Algorithm because we always have M <= N.

        min_v, max_v = min(nums), max(nums)
        m = max_v - min_v + 1
        cnt = [0] * m

        for x in nums:
            cnt[x - min_v] += 1

        for i in reversed(range(m)):
            k -= cnt[i]
            if k <= 0:
                return i + min_v

        return -1



        ## S4: Quick Select 
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
        