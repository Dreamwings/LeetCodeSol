class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        
        ## S1: Sliding Window, Two Pointers
        ## T: O(N)
        ## S: O(M), M is the total length of all forbidden substrings combined.

        forbidden_set = set(forbidden)
        res = 0
        right = len(word) - 1
        
        # Traverse from right to left
        for left in range(len(word) - 1, -1, -1):
            # Note that 1 <= forbidden[i].length <= 10, so the below loop is O(10) at most
            for k in range(left, min(left + 10, right + 1)): 
                if word[left:k+1] in forbidden_set:
                    right = k - 1
                    break
            res = max(res, right - left + 1)
        return res