class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        
        ## S1: Binary Search
        ## T: O(N*logM)
        ## S: O(1)

        # find the max and min value in arr
        # do binary search between 1 and max to check if mid can reach k segments

        # write a function to check if a mid length meets requirement
        def check(mid):
            cnt = 0
            for x in ribbons:
                cnt += x // mid
            return cnt >= k

        lo, hi = 1, max(ribbons)
        # lo must be set to 1 instead of 0, otherwise it might cause 0 division error

        while lo <= hi:
            m = (lo + hi) // 2
            if check(m):
                lo = m + 1
            else:
                hi = m - 1

        return lo - 1