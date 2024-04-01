class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        ## S1: From right to left

        # Initialize i to the last index of the string
        i = len(s) - 1
      
        # Skip any trailing spaces
        while i >= 0 and s[i] == ' ':
            i -= 1
      
        # i now points to the last character of the last word
        j = i
      
        # Find the space before the start of the last word
        while j >= 0 and s[j] != ' ':
            j -= 1
      
        # The length of the last word is the difference between i and j
        return i - j