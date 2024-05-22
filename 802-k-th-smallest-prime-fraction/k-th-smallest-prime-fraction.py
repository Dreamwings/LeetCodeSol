class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        
        ## S2: Binary Search
        ## T: O(NlogM), N = len(arr), M = max(arr)
        ## S: O(1)

        n = len(arr)
        lo, hi = 0, 1.0
        
        # Binary search for finding the kth smallest prime fraction
        while lo < hi:
            # Calculate the middle value
            mid = (lo + hi) / 2
            # Initialize variables to keep track of maximum fraction and indices
            max_frac = 0.0
            smaller_frac = 0
            num, den = 0, 0 # numerator_idx, denominator_idx
            j = 1
            
            # Iterate through the array to find fractions smaller than mid
            for i in range(n - 1):
                while j < n and arr[i] >= mid * arr[j]:
                    j += 1

                # Count smaller fractions
                smaller_frac += (n - j)

                # If we have exhausted the array, break
                if j == n:
                    break

                # Calculate the fraction
                fraction = arr[i] / arr[j]

                # Update max_frac and indices if necessary
                if fraction > max_frac:
                    num = i
                    den = j
                    max_frac = fraction

            # Check if we have found the kth smallest prime fraction
            if smaller_frac == k:
                return [arr[num], arr[den]]
            elif smaller_frac > k:
                hi = mid  # Adjust the range for binary search
            else:
                lo = mid  # Adjust the range for binary search
                
        return []  # Return empty list if kth smallest prime fraction not found
        
        
        ## S1: Priority Queue
        ## T: O((N+K)logN)
        ## S: O(N)

        # Create a priority queue to store pairs of fractions
        pq = []

        # Custom comparator for priority queue
        def compare(a, b):
            return a[0] - b[0]

        # Push the fractions formed by dividing each element by
        # the largest element into the priority queue
        for i in range(len(arr) - 1):
            heapq.heappush(pq, ((arr[i] / arr[-1]), i, len(arr) - 1))

        # Iteratively remove the top element (smallest fraction) 
        # and replace it with the next smallest fraction
        for _ in range(k - 1):
            cur = heapq.heappop(pq)
            numerator_index = cur[1]
            denominator_index = cur[2] - 1
            if denominator_index > numerator_index:
                heapq.heappush(pq, (
                    (arr[numerator_index] / arr[denominator_index]), 
                    numerator_index, 
                    denominator_index
                ))

        # Retrieve the kth smallest fraction from 
        # the top of the priority queue
        result = heapq.heappop(pq)
        return [arr[result[1]], arr[result[2]]]


