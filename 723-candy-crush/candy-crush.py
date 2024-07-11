class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        
        ## S1:
        ## T: O((MN)^2)
        ## S: O(1)

        m, n = len(board), len(board[0])
      
        # Flag to indicate if we should continue crushing candies
        should_crush = True
      
        # Keep crushing candies until no more moves can be made
        while should_crush:
            should_crush = False  # Reset the flag for each iteration
          
            # Mark the candies to be crushed horizontally
            for r in range(m):
                for c in range(n - 2):
                    v = abs(board[r][c])
                    # Check if three consecutive candies have the same value
                    if v != 0 and v == abs(board[r][c + 1]) == abs(board[r][c + 2]):
                        should_crush = True  # We will need another pass after crushing
                        # Mark the candies for crushing by negating their value
                        board[r][c] = board[r][c + 1] = board[r][c + 2] = -v
                      
            # Mark the candies to be crushed vertically
            for c in range(n):
                for r in range(m - 2):
                    v = abs(board[r][c])
                    # Check if three consecutive candies vertically have the same value
                    if v != 0 and v == abs(board[r + 1][c]) == abs(board[r + 2][c]):
                        should_crush = True  # We will need another pass after crushing
                        # Mark the candies for crushing
                        board[r][c] = board[r + 1][c] = board[r + 2][c] = -v
                      
            # Drop the candies to fill the empty spaces caused by crushing
            if should_crush:
                for c in range(n):
                    # Pointer to where the next non-crushed candy will fall
                    write_row = m - 1
                    for r in range(m - 1, -1, -1):
                        # If the candy is not marked for crushing, bring it down
                        if board[r][c] > 0:
                            board[write_row][c] = board[r][c]
                            write_row -= 1
                    # Fill the remaining spaces at the top with zeros
                    while write_row >= 0:
                        board[write_row][c] = 0
                        write_row -= 1
                      
        return board
