class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        
        ## S1: Greedy, DP with Sorting

        m, n = len(matrix), len(matrix[0])
        max_area = 0

        # Update the matrix such that each cell in the matrix represents the height 
        # of the histogram that can be formed with the base at that cell
        for row in range(1, m):
            for col in range(n):
                if matrix[row][col]:
                    matrix[row][col] = matrix[row - 1][col] + 1
        
        for row in matrix:
            # Sort each row in descending order to facilitate the calculation 
            # of the maximum rectangle in the histogram
            row.sort(reverse=True)
            # Iterate over each value in the sorted row to calculate the maximum area
            # Each value in the sorted row corresponds to the height of a bar in the histogram,
            # and its index represents potential width of the rectangle at that height
            for i, height in enumerate(row):
                width = i + 1
                area = width * height
                max_area = max(max_area, area)

        return max_area