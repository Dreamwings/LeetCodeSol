class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        ## S1: HashMap + Sorting
        ## T: O(NlogN)
        ## S: O(N)

        d = collections.defaultdict(int)
        
        for x, fr, to in trips:
            d[fr] += x
            d[to] -= x
        
        cnt = 0
        
        for k in sorted(d):
            cnt += d[k]
            if cnt > capacity:
                return False
        
        return True

        """

        ## S2: Bucket Sort
        ## T: O(M + N), M = 1001
        ## S: O(M) ~ O(1)

        location_deltas = [0] * 1001
      
        # Loop over each trip in the trips list
        for passengers, start_location, end_location in trips:
            # Increase the passenger count at the start location
            location_deltas[start_location] += passengers
            # Decrease the passenger count at the end location
            location_deltas[end_location] -= passengers
      
        # Use accumulate to calculate the running total of passengers at each location
        # and verify if at any point the capacity is exceeded
        # all() will return True if all running totals are less than or equal to capacity
        return all(current_passengers <= capacity for current_passengers in accumulate(location_deltas))
        
        """