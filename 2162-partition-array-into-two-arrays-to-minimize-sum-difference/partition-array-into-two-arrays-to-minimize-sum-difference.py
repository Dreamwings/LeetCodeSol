class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        
        ## S1: Meet in the Middle
        ## T: O(N * 2^N) + O(2**M1 * logM2 + M2 * logM2), 2*M1 subset sums for left, M2 right len
        ## S: O(2 * 2^N)

        n = len(nums) // 2 # Note this is n/2, ie no. of elements required in each.
        
        def cal_sums(nums): # Calculate all combinations sum of k elements
            comb_sum = {}
            n = len(nums)
            for k in range(1, n+1): # takes k element for nums
                sums = []
                for comb in combinations(nums, k):
                    s = sum(comb)
                    sums.append(s)
                comb_sum[k] = sums
            return comb_sum
        
        left_part, right_part = nums[:n], nums[n:]
        left_sums, right_sums = cal_sums(left_part), cal_sums(right_part)
        # the case when taking all n from left_part for left_res, and vice versa
        res = abs(sum(left_part) - sum(right_part)) 
        total = sum(nums) 
        half = total // 2 # the best sum required for each, we have to find sum nearest to this
        for k in range(1, n):
            left = left_sums[k] # if taking k no. from left_sums
            right = right_sums[n-k] # then we have to take remaining n-k from right_sums.
            right.sort() # sorting, so that we can binary search the required value
            for x in left:
                r = half - x # required, how much we need to add in x to bring it closer to half.
                # we are finding index of value closest to r, present in right, using binary search
                p = bisect.bisect_left(right, r) 
                for q in [p, p-1]:
                    if 0 <= q < len(right):
                        left_res_sum = x + right[q]
                        right_res_sum = total - left_res_sum
                        diff = abs(left_res_sum - right_res_sum)
                        res = min(res, diff) 
        return res