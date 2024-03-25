class Solution:
    def maximumSwap(self, num: int) -> int:
        
        from collections import defaultdict
        
        a = list(map(int, str(num)))  # note in Python 3, need to use list for map function
        # a = [int(x) for x in str(num)]
        last = defaultdict(int)
        for i, x in enumerate(a):
            last[x] = i
        
        for i, x in enumerate(a):
            for n in range(9, x, -1):
                if last[n] > i:
                    a[i], a[last[n]] = a[last[n]], a[i]
                    return int(''.join([str(x) for x in a]))
        
        return num