class Solution:
    def maxRepOpt1(self, text: str) -> int:
        
        ## S1: Sliding Window
        ## T: O(N^2)
        ## S: O(26) -> O(1)

        d = Counter(text)  # Count the frequency of each character in the given text
        n = len(text)     # Length of the given text
        max_length = i = 0  # Initialize max_length and i to zero

        # Iterate through the text to find the maximum length of a repeating character substring
        while i < n:
            j = i
            # Find the end of the current sequence of same characters
            while j < n and text[j] == text[i]:
                j += 1
            # Calculate the length of this sequence
            left_len = j - i
          
            # Find the next sequence of the same character after a different one
            k = j + 1
            while k < n and text[k] == text[i]:
                k += 1
            # Calculate the length of the second sequence
            right_len = k - j - 1
          
            # Calculate the maximum length by using the sequences found and the overall character count
            # We can insert at most one character from other parts of the string
            total_length = min(left_len + right_len + 1, d[text[i]])
          
            # Update the max_length if the current total_length is greater
            max_length = max(max_length, total_length)
          
            # Move the i to the end of the first sequence
            i = j
      
        return max_length

