class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        ## S1: DP
        ## Time: O(query_row^2)
        ## Space:  O(101 * 101) -> O(1)

        tower = [[0.0] * 101 for _ in range(101)]
        tower[0][0] = poured  # top glass
      
        # Simulating the pouring process up to the query_row + 1
        for row in range(query_row + 1):
            for col in range(row + 1):
                # If there's an overflow in the current glass...
                if tower[row][col] > 1:
                    # Calculate the champagne that flows to each glass below.
                    overflow = (tower[row][col] - 1) / 2.0
                    # Reset the current glass to full after overflow.
                    tower[row][col] = 1
                    # Distribute the overflowed champagne to the two glasses below.
                    tower[row + 1][col] += overflow
                    tower[row + 1][col + 1] += overflow
      
        # Return the amount of champagne in the glass at query_row and query_glass, capped at 1.
        return min(1, tower[query_row][query_glass])
