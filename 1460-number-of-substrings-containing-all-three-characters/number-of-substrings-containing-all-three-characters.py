class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        ## S1: Sliding Window
        ## T: O(N)
        ## S: O(1)

        # Keep track of the last seen index of 'a', 'b', and 'c'
        last_seen_index = {"a": -1, "b": -1, "c": -1}
        res = 0
        
        for i, c in enumerate(s):
            # Update the last seen index for the current character
            last_seen_index[c] = i
            # Increment the res by one more than the smallest last seen index among 'a', 'b', and 'c'
            # This is because a valid substring must include at least one of each
            res += min(last_seen_index.values()) + 1

        # Return the total count of valid substrings that contain at least one of each 'a', 'b', and 'c'
        return res        