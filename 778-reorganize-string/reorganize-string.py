class Solution:
    def reorganizeString(self, s: str) -> str:
        
        from collections import Counter
        from heapq import heapify, heappop, heappush

        ## S2: Heap
        ## T: O(N + NlogN)
        ## S: O(N)
        
        n = len(s)
        d = Counter(s)
      
        # If the max frequency is more than half of the string length, round up,
        # then the task is impossible as that character would need to be adjacent to itself.
        if max(d.values()) > (n + 1) // 2:
            return ''
        
        i = 0 # Initialize i for placing characters
        res = [None] * n # Create a list to store the res string
      
        # Fill in the characters, starting with the most common
        for char, freq in d.most_common():
            while freq:
                # Place the character at the current i
                res[i] = char
                # Decrease the frequency count
                freq -= 1
                # Move to the next even i as i starts from 0
                i += 2
                # Move to the first odd i if the end is reached
                if i >= n:
                    i = 1
            # print(res)
        return ''.join(res)

        
        """

        ## S1: MaxHeap
        
        n = len(s)
        if n == 0 or n == 1: return s
        
        d = Counter(s)
        res = ''
        if max(d.values()) > (n + 1) // 2: return res
        
        hq = [(-v, c) for c, v in d.items()]
        heapify(hq)
        
        i, x = 0, ''
        
        while hq:
            j, y = heappop(hq)
            res += y
            j += 1
            
            if i < 0:
                heappush(hq, (i, x))
            
            i, x = j, y
            
        return  res
        """