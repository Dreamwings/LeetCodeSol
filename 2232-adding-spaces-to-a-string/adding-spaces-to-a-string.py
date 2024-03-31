class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        
        ## S1:

        answer = []
        # Pointer to track the index within the 'spaces' list
        j = 0
      
        # Iterate over the characters and indices of the input string 's'
        for i, char in enumerate(s):
            # Check if the current index matches the next space position
            # and that we have not used all the provided spaces
            if j < len(spaces) and i == spaces[j]:
                # If so, append a space to the 'answer' list
                answer.append(' ')
                # Move the pointer to the next space position
                j += 1
            # Append the current character to the 'answer' list
            answer.append(char)
      
        # Join all elements of 'answer' to get the final string with spaces
        return ''.join(answer)