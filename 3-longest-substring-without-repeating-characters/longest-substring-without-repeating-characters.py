class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        ## S1: Sliding Window
        ## T: O(N)
        ## S: O(min(M, N)) ~ O(1) as the num of char has a max value

        if not s: return 0
        seen = collections.defaultdict(int) # k: v, to store the last index v of char k
        i, res = 0, 0

        for j, c in enumerate(s):
            if c in seen and i <= seen[c]: # means c is repeated now
                i = seen[c] + 1
            else:
                res = max(res, j - i + 1)
            seen[c] = j

        return res

        