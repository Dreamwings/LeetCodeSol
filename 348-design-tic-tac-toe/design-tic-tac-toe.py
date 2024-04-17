class TicTacToe:

    ## S2: https://algo.monster/liteproblems/348
    
    ## S1: 

    def __init__(self, n: int):
        self.n = n
        self.r = [0] * n
        self.c = [0] * n
        self.diag = [0, 0]
        
    def move(self, row: int, col: int, player: int) -> int:
        score = 1 if player == 1 else -1
        self.r[row] += score
        self.c[col] += score
        if row == col:
            self.diag[0] += score
        if row + col == self.n - 1:
            self.diag[1] += score
        for s in (self.r[row], self.c[col], *self.diag):
            if abs(s) == self.n:
                return 1 if s > 0 else 2
        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)