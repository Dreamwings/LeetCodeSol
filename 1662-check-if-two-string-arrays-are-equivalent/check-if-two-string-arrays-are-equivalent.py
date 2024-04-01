class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        ## S1: Concatenate

        return ''.join(word1) == ''.join(word2)

        ## S2: Two Pointers

        w1, w2, i, j = '', '', 0, 0
        while word1 or word2:
            if i >= len(w1): w1, i = word1.pop(), 0
            if j >= len(w2): w2, j = word2.pop(), 0
            if w1[-1-i] != w2[-1-j]: return False
            i, j = i+1, j+1
        return True
    