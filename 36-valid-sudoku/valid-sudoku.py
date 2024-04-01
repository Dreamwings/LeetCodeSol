class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        ## S1: HashSet

        # Create tracking structures for rows, columns, and 3x3 sub-boxes.
        rows = [[False] * 9 for _ in range(9)]
        cols = [[False] * 9 for _ in range(9)]
        boxes = [[False] * 9 for _ in range(9)]

        # Iterate over each cell in the 9x9 board.
        for i in range(9):
            for j in range(9):
                cell_value = board[i][j]
                # Skip checking if the cell is empty.
                if cell_value == '.':
                    continue
              
                # Convert str digit to int and adjust index to zero-based.
                num = int(cell_value) - 1
              
                # Calculate box index for 3x3 sub-boxes using integer division.
                box_index = (i // 3) * 3 + j // 3
              
                # If the number has already been encountered in current
                # row, column or box, sudoku condition is violated.
                if rows[i][num] or cols[j][num] or boxes[box_index][num]:
                    return False
              
                # Mark current num as encountered in current row, column and box.
                rows[i][num] = True
                cols[j][num] = True
                boxes[box_index][num] = True

        # If no conditions are violated, then the board is a valid sudoku.
        return True