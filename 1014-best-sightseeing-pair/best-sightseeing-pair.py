class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ## S1: DP
        ## T: O(N)
        ## S: O(1)
        max_score = 0  # Initialize the maximum score to zero
        max_value_plus_index = values[0]  # Initialize to the first value plus its index (0)

        # Iterate over the array, starting from the second element (index 1)
        for i in range(1, len(values)):
            # Update the max score using the current value and the best previous value plus index found
            max_score = max(max_score, values[i] - i + max_value_plus_index)
            # Update the max_value_plus_index with the maximum of the current and the previous
            # while accounting for the increasing index
            max_value_plus_index = max(max_value_plus_index, values[i] + i)

        # Return the maximum score found for any sightseeing pair
        return max_score