class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
        ## S2:
        ## https://leetcode.com/problems/heaters/solutions/95875/short-python/
        ## T: O(MlogM + NlogN) ?


        heaters = sorted(heaters) + [float('inf')]
        i = res = 0
        for x in sorted(houses):
            while x >= sum(heaters[i:i+2]) / 2.:
                i += 1
            res = max(res, abs(heaters[i] - x))
        return res




        ## S1: Sorting + Two Pointers + Binary Search
        ## T: O(MlogM + NlogN + (M + N)log(max(houses) - min(houses)))
        ## S: O(M + N)

        # First, sort the houses and heaters to enable efficient scanning
        houses.sort()
        heaters.sort()

        # The function 'can_cover' checks if a given radius 'radius'
        # is enough to cover all houses by heaters. Returns True if it is, False otherwise.
        def can_cover(radius):
            # Get the number of houses and heaters
            num_houses, num_heaters = len(houses), len(heaters)
            house_idx, heater_idx = 0, 0   # Start scanning from the first house and heater

            # Iterate over all houses to check coverage
            while house_idx < num_houses:
                # If no more heaters are available to check, return False
                if heater_idx >= num_heaters:
                    return False

                # Calculate the minimum and maximum coverage range of the current heater
                min_range = heaters[heater_idx] - radius
                max_range = heaters[heater_idx] + radius

                # If the current house is not covered, attempt to use the next heater
                if houses[house_idx] < min_range:
                    return False
                # If the current house is outside the current heater's max range,
                # move to the next heater
                if houses[house_idx] > max_range:
                    heater_idx += 1
                else: # Otherwise the house is covered, move to the next house
                    house_idx += 1

            return True  # All houses are covered

        # Start with a radius range of 0 to a large number (1e9 is given as a maximum)
        left, right = 0, int(1e9)
      
        # Perform a binary search to find the minimum radius
        while left < right:
            mid = (left + right) // 2  # Choose the middle value as the potential radius
            # If all houses can be covered with the 'mid' radius, search the lower half
            if can_cover(mid):
                right = mid
            else: # If not, search the upper half
                left = mid + 1
      
        # The minimum radius required to cover all houses is 'left' after the loop
        return left
