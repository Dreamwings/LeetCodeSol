class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        
        ## S2: DP + Heap with Optimal Space
        ## T: O(M*N)
        ## S: O(1)

        for i in range(1, len(grid)):
            r = heapq.nsmallest(2, grid[i - 1])
            for j in range(len(grid[0])):
                grid[i][j] += r[1] if grid[i - 1][j] == r[0] else r[0]
        return min(grid[-1])
        


        ## S1: DP with Optimal Space
        ## T: O(M*N)
        ## S: O(1)
        
        min_sum = min_sum_2nd = float('inf')
        min_pos = -1
      
        # Iterate over each row in the matrix.
        for row in grid:
            # Initialize the smallest and second smallest falls of the current row
            # ("cur_min" and "cur_min_2nd"), and the position of
            # the smallest fall in the current row ("cur_min_pos").
            cur_min = cur_min_2nd = float('inf')
            cur_min_pos = -1
          
            # Iterate over each value in the current row with its index.
            for i, v in enumerate(row):
                # Determine whether to use the smallest or second smallest fall from
                # the previous row to add to the current element.
                pre_sum = min_sum_2nd if i == min_pos else min_sum
                tot_sum = v if pre_sum == float('inf') else pre_sum + v
                # Update the smallest or second smallest fall if necessary.
                if tot_sum < cur_min:
                    cur_min_2nd = cur_min
                    cur_min = tot_sum
                    cur_min_pos = i
                elif tot_sum < cur_min_2nd:
                    cur_min_2nd = tot_sum
          
            # Move to the next row: update the smallest and second smallest falls and the position
            min_sum, min_sum_2nd, min_pos = cur_min, cur_min_2nd, cur_min_pos
        
        return min_sum
        