class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        
        ## S1: Counting Sort
        ## T: O(N)
        ## S: O(N)

        n = len(arr)
        counts = [0] * (n + 1) # counts[x] is equal to the frequency of x in arr
        # Note we don't care any num > n, as we'll treat them as n.
        # E.g. arr = [100,1,1000], counts = [0, 1, 0, 2], both 100 and 1000 count as n=3
        
        for num in arr:
            counts[min(num, n)] += 1
        print(counts)
        ans = 1
        for num in range(2, n + 1):
            # Two cases:
            # 1. ans + count[num] <= num: [1, 2, 3, 100, 100], two 100s can be reduced to 4 and 5 to improve the res
            # 2. ans + count[num] > num: [1, 3, 3, 3, 3, 3, 3], we can't improve the result, ans = max num
            ans = min(ans + counts[num], num)
    
        return ans

        """
        ## S2: Sorting
        ## T: O(NlogN)
        ## S: O(1)

        arr.sort() # O(NlogN)
        prev = 1 # 1st value must be 1

        for x in arr[1:]:
            prev = min(x, prev + 1)

        return prev
        """
