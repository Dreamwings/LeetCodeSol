class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        """
        ## S1:

        str=" ".join(sentence) + " "
        valid_space = 0
        for i in range(rows):
            valid_space += cols
            if str[valid_space%len(str)] == " ":
                valid_space += 1
            else:
                while valid_space > 0 and str[valid_space%len(str) - 1] != " ":
                    valid_space-=1
        return valid_space // len(str)

        
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

        """
        ## S2: Binary Search
        ## T: O(R*logN)
        ## S: O(N)

        prefix = [0]
        for x in sentence: prefix.append(prefix[-1] + len(x) + 1)
        
        ans = j = 0
        for i in range(rows): 
            n = prefix[-1] - prefix[j]
            if n > cols+1: 
                j = bisect_right(prefix, prefix[j]+cols+1)-1
            elif n <= cols+1: 
                q, r = divmod(cols+1-n, prefix[-1])
                ans += 1+q
                j = bisect_right(prefix, r)-1
        return ans     