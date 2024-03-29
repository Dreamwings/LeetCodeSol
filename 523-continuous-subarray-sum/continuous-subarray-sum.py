class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        ## S1: 
        
        # note that k >= 1
        # use dict d to store the remainder of presum mod k and its first index
        # key is remainder, value is index
        d = {0: -1}
        s = 0
        
        for i, x in enumerate(nums):
            s += x
            s %= k
            if s not in d:
                d[s] = i
            else:
                if i - d[s] >= 2:
                    return True
        
        return False

        """
        ## S2
        
        from collections import defaultdict
        
        mod_id = defaultdict(list)
        pre_s = 0
        
        for i, x in enumerate(nums):
            pre_s += x
            m = pre_s % k
            mod_id[m].append(i)
        
        # check if any mod_id[i] has at least two elements
        # we also need to check the two elements are not neighbors
        # one special case is mod_id[0], which means a presum from nums[0] to nums[i]
        
        for idx in mod_id[0]:
            if idx >= 1:
                return True
        
        for m, arr in mod_id.items():
            if m == 0:
                continue
            if len(arr) < 2:
                continue
            # now we check the case for m > 0 and len(arr) >= 2
            # idx of presum actually appended into mod_id[m] in order
            # so just need to check if the diff of last idx and first idx is larger than 1
            if arr[-1] - arr[0] > 1:
                return True
        
        return False
        """        
        