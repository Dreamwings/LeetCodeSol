from collections import defaultdict
from sortedcontainers import SortedDict
from bisect import bisect_right

## S3: Hash Table + Array + Binary Search
## T: 
##   set(): O(L) for a single call, L is average length of key and value strings, logM for SortedDict
##   get(): O(L⋅logM) for a single call
## S:
##   set(): O(L) for a single call
##   get(): O(1) for a single call, no additional space needed

class TimeMap:
    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Append the (timestamp, value) tuple to the list corresponding to the key.
        self.d[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        # If the key does not exist in the dictionary, return an empty string.
        if key not in self.d:
            return ''
      
        # Do binary search
        arr = self.d[key]
        l, r = 0, len(arr) - 1
        
        while l <= r:
            m = (l + r) >> 1
            if arr[m][0] <= timestamp:
                l = m + 1
            else:
                r = m - 1
                
        if r == -1: return ''
        return arr[r][1]



## S1: Hash Table + Array + Binary Search
## T: 
##   set(): O(L) for a single call, L is average length of key and value strings, logM for SortedDict
##   get(): O(L⋅logM) for a single call
## S:
##   set(): O(L) for a single call
##   get(): O(1) for a single call, no additional space needed

class TimeMap:
    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Append the (timestamp, value) tuple to the list corresponding to the key.
        self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # If the key does not exist in the dictionary, return an empty string.
        if key not in self.d:
            return ''
      
        # Retrieve the list of (timestamp, value) tuples for the given key.
        time_value_pairs = self.d[key]
      
        # Use bisect_right to find the index where the timestamp would be inserted
        # to maintain the list in sorted order. Since the list is sorted by timestamp,
        # and we want to find the largest timestamp less than or equal to the given timestamp,
        # we use (timestamp, chr(127)) as a "high" value to ensure we can locate
        # timestamps that are equal to the given one.
        index = bisect_right(time_value_pairs, (timestamp, chr(127)))
      
        # If index is 0, there is no timestamp less than or equal to the given timestamp,
        # so we return an empty string. If not, we return the value corresponding to 
        # the timestamp immediately before the insertion point, which would be index - 1.
        return time_value_pairs[index - 1][1] if index else ''



## S2: Hash Table + Sorted Map + Binary Search
## T: 
##   set(): O(L⋅logM) for a single call, L is average length of key and value strings, logM for SortedDict
##   get(): O(L⋅logM + logM) for a single call
## S:
##   set(): O(L) for a single call
##   get(): O(1) for a single call, no additional space needed

class TimeMap:
    def __init__(self):
        self.d = defaultdict(SortedDict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # If the 'key' does not exist in dictionary.
        # if not key in self.d:
        #     self.d[key] = SortedDict()
            
        # Store '(timestamp, value)' pair in 'key' bucket.
        self.d[key][timestamp] = value
        

    def get(self, key: str, timestamp: int) -> str:
        # If the 'key' does not exist in dictionary we will return empty string.
        if not key in self.d:
            return ""
        
        it = self.d[key].bisect_right(timestamp)
        # If iterator points to first element it means, no time <= timestamp exists.
        if it == 0:
            return ""
        
        # Return value stored at previous position of current iterator.
        return self.d[key].peekitem(it - 1)[1]
        



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)