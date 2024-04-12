class Solution:
    def trap(self, height: List[int]) -> int:
        
        
        ## S1: Two Pointers
        ## every time move the pointer with a lower boundh
        ## T: O(N)
        ## S: O(1)

        n = len(height)
        i, j = 0, n - 1
        l, r = height[i], height[j]
        res = 0

        while i < j:
            h = min(l, r)
            if l == h:
                res += max(0, h - height[i])
                i += 1
                l = max(l, height[i])
            else:
                res += max(0, h - height[j])
                j -= 1
                r = max(r, height[j])
        return res

        """

        ## S2: DP
        ## T: O(N)
        ## S: O(N)

        n = len(height)

        # Initialize arrays to store the maximum to the left and right of each element.
        max_left = [height[0]] * n
        max_right = [height[-1]] * n

        # Fill the max_left array with the maximum height to the left of each element.
        for i in range(1, n):
            max_left[i] = max(max_left[i - 1], height[i])

        # Fill the max_right array with the maximum height to the right of each element.
        for i in range(n - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], height[i])

        # Calculate the total amount of trapped water using the height difference
        # between the minimum of max_left and max_right for each element and the height at that element.
        trapped_water = sum(min(max_left[i], max_right[i]) - height[i] for i in range(n))

        # Return the total amount of trapped water.
        return trapped_water

        """
