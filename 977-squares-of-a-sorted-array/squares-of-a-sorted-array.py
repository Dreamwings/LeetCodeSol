class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        ## S2: Two Pointers
        n = len(nums)
        res = [0] * n
        i, j, k = 0, n - 1, n - 1
        
        while i <= j:
            x, y = nums[i] ** 2, nums[j] ** 2
            if x >= y:
                res[k] = x
                i += 1
            else:
                res[k] = y
                j -= 1
            k -= 1

        return res
        
        """
        ## S1: Two Pointers

        n = len(nums)
        res = []
        i, j = 0, n - 1
        
        while i <= j:
            x, y = nums[i] ** 2, nums[j] ** 2
            if x >= y:
                res.append(x)
                i += 1
            else:
                res.append(y)
                j -= 1
        
        return reversed(res)
        """