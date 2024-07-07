class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:

        ## S1: Binary Search
        ## T: O(R*logN), R = rows, N = len(sentence)
        ## S: O(N)

        prefix = [0] # To store the prefix sum of word length (+ 1 space)
        for x in sentence: 
            prefix.append(prefix[-1] + len(x) + 1)
        
        ans = j = 0 # j is the current word index that have been (can be) filled
        for i in range(rows): 
            n = prefix[-1] - prefix[j] # Num of char needed for the left sentence
            if n > cols + 1: # Current row is not enough
                # Use 1 more row, find which word can be filled
                j = bisect_right(prefix, prefix[j] + cols + 1) - 1
            elif n <= cols + 1: # Current row can handle left sentence
                q, r = divmod(cols + 1 - n, prefix[-1])
                ans += 1 + q
                j = bisect_right(prefix, r) - 1
            # print(n, j)
        return ans     

        

        ## S2:
        ## T: O(R * C) for worst case, R = rows, C = cols
        ## S: O(M), M is the total length of the string with spaces

        # Combine the sentence into a single string with spaces and an extra space at the end
        s = " ".join(sentence) + " "
        m = len(s)
        cur_pos = 0  # Start at the beginning of the concatenated sentence
      
        # Iterate over each row
        for _ in range(rows):
            # Move the current position forward by the number of columns
            cur_pos += cols
          
            # If the current character is a space, it fits perfectly and move to next character 
            if s[cur_pos % m] == " ":
                cur_pos += 1
            # If not, backtrack to the last space so that the word doesn't break
            while cur_pos > 0 and s[(cur_pos - 1) % m] != " ":
                cur_pos -= 1
      
        # Return the number of times the sentence was fully fitted in the rows and columns
        return cur_pos // m


        
        ## S3: DP

        n = len(sentence)
        dp = [0] * n
        #dp[i] denotes if a new row starts with word[i], # of words we can put there, inclusive
        for i in range(n):
            length = cols
            j = i 
            while len(sentence[j % n]) <= length:
                length = length - len(sentence[j % n]) - 1
                j += 1
            dp[i] = j - i 
        
        k, index = 0, 0 #initialization 
        total = 0 
        for k in range(rows):
            total += dp[index]
            index = (index + dp[index % n]) % n
        return total//n

        