class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        from collections import Counter
        
        ## S1:
        ## T: O(N^2)
        ## S: O(1)

        # Get the size of the grid
        n = len(grid)

        # Initialize counters for each part of the "Y"
        vert_horiz_counter = Counter()
        non_Y_counter = Counter()

        # Iterate over the grid to count the occurrences in the "Y" shape and elsewhere
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                # Calculate which part of the grid is the 'Y' shape
                is_vert_or_first_diag = i == j and i <= n // 2
                is_second_diag = i + j == n - 1 and i <= n // 2
                is_horiz_middle = j == n // 2 and i >= n // 2
              
                # Count the occurrences
                if is_vert_or_first_diag or is_second_diag or is_horiz_middle:
                    vert_horiz_counter[x] += 1
                else:
                    non_Y_counter[x] += 1

        # Compute the minimum operations by finding max occurrence in 'Y' and 
        # outside 'Y', excluding the same number in both places
        min_ops = min(
            n * n - vert_horiz_counter[i] - non_Y_counter[j] 
            for i in range(3) for j in range(3) if i != j
        )

        return min_ops