class Solution:
    def partitionString(self, s: str) -> int:
        
        ## S2:
        ## T: O(N)
        ## S: O(1)

        res = 1
        used_char = 0 # keep track of the characters used in the current partition.
      
        for c in s:
            # Calculate the bit index corresponding to the character.
            c_idx = ord(c) - ord('a')
          
            # Check if the character has already been used in the current partition.
            # (v >> i) & 1 checks if the ith bit in 'used_char' is set to 1,
            # meaning that character was already used.
            if (used_char >> c_idx) & 1:
                # If so, we need a new partition. Reset 'used_char' and
                # increment the 'res' counter.
                used_char = 0
                res += 1
          
            # Set the bit at the character's index to 1 to mark it as used for the current partition.
            used_char |= 1 << c_idx
      
        return res

        
        
        ## S1:
        ## T: O(N)
        ## S: O(1)

        lastSeen = [-1]*26
        count = 1
        substringStarting = 0

        for i in range(len(s)):
            if lastSeen[ord(s[i]) - ord('a')] >= substringStarting:
                count += 1
                substringStarting = i
            lastSeen[ord(s[i]) - ord('a')] = i

        return count

