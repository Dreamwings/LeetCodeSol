class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        
        ## S2: 


        n = len(s)
      
        # Prefix sum array counts the number of plates ('*') up to index 'i'
        pre_sum = [0] * (n + 1)
        for i, char in enumerate(s):
            pre_sum[i + 1] = pre_sum[i] + (char == '*')

        # Arrays to store the index of the closest candle to the left and right
        closest_left = [0] * n
        closest_right = [0] * n
        left_candle_idx = right_candle_idx = -1
        for i, char in enumerate(s):
            if char == '|':
                left_candle_idx = i
            closest_left[i] = left_candle_idx

        # Populate the closest_right array in reverse
        for i in range(n - 1, -1, -1):
            if s[i] == '|':
                right_candle_idx = i
            closest_right[i] = right_candle_idx

        res = [0] * len(queries)

        for k, (l_edge, r_edge) in enumerate(queries):
            # Find the closest right candle for the left edge
            # And the closest left candle for the right edge
            candle_to_the_right = closest_right[l_edge]
            candle_to_the_left = closest_left[r_edge]

            # If valid candle indexes are found and they do not overlap
            if candle_to_the_right >= 0 and candle_to_the_left >= 0 and candle_to_the_right < candle_to_the_left:
                res[k] = pre_sum[candle_to_the_left] - pre_sum[candle_to_the_right + 1]

        return res

        """

        ## S1: Binary Search
        ## T: O(N + Q*logN)
        ## S: O(N + Q)

        # Find out indices of candies and add them to a list A
        # For each query [a,b],
        # find out the candies after a and the candies before b.

        # A[i] - A[j] + 1 is the length between two candies,
        # i - j + 1is the number of candies.
        # (A[j] - A[i]) - (j - i) is the number of plates between two candies.

        A = [i for i, c in enumerate(s) if c == '|']
        res = []
        for a, b in queries:
            i = bisect.bisect_left(A, a)
            j = bisect.bisect(A, b) - 1
            res.append((A[j] - A[i]) - (j - i) if i < j else 0)
        return res

        """