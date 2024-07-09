class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        
        ## S1:
        ## T: O(M * N * K), K = len(word)
        ## S: O(M * N)

        n = len(word)
        
        for mat in board, list(zip(*board)):
            for row in mat:
                arr = "".join(row).split("#")
                # print("".join(row), arr)
                for s in arr:
                    for w in [word, word[::-1]]:
                        if len(s) == n and all(s[i] == w[i] or s[i] == " " for i in range(n)):
                            return True
        return False

