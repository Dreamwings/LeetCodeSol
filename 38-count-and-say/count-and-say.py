class Solution:
    def countAndSay(self, n: int) -> str:
        

        ## S1: 
        ## T: O(2^N)
        ## S: O(2^N)

        s = '1'
      
        # Build the s up to the n-th term.
        for _ in range(n - 1):
            i = 0
            tmp = [] # Create a temporary list to hold new term
          
            # Iterate through the current s to build the next s
            while i < len(s):
                cnt = i
                # Count the number of same digits
                while cnt < len(s) and s[cnt] == s[i]:
                    cnt += 1
              
                # Append the count and the digit itself to the tmp list
                tmp.append(str(cnt - i))
                tmp.append(s[i])
              
                # Move to the next different digit
                i = cnt
          
            # Join the tmp list to make a string and assign it as the new s
            s = ''.join(tmp)
      
        # After the loop, s variable holds the n-th term of the s
        return s

        """
        ## S2:
        ## T: O(2^N)
        ## S: O(2^N)

        if n == 0: return ''
        if n == 1: return '1'
        
        s = '1'
        
        for _ in range(n-1):
            prev, count = s[0], 0
            nxt = ''
            for l in s:
                if prev != l:
                    nxt += str(count) + prev
                    prev, count = l, 1
                else: count += 1
					
            nxt += str(count) + prev
            s = nxt
        
        return s
        """