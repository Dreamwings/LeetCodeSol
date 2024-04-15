## S2: Ordered Dictionary
## T: O(1) for get and put
## S: O(N)

class LRUCache:

    from collections import OrderedDict
    
    def __init__(self, capacity: int):
        self.n = capacity
        self.d = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        val = self.d[key]
        del self.d[key]
        self.d[key] = val
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            del self.d[key]
        self.d[key] = value
        if len(self.d) > self.n:
            self.d.popitem(last=False)



## S1: Double Linked List
## T: O(1) for get and put
## S: O(N)
    
class LRUCache:

    def __init__(self, capacity: int):
        self.n = capacity
        self.d = {}
        self.prev, self.next = {}, {}
        self.head, self.tail = "H", "T"
        self.connect(self.head, self.tail)
    
    def connect(self, A, B):
        self.prev[B] = A
        self.next[A] = B
    
    def delete(self, key):
        self.connect(self.prev[key], self.next[key])
        del self.d[key], self.prev[key], self.next[key]
    
    def add(self, key, val):
        self.d[key] = val
        self.connect(self.prev["T"], key)
        self.connect(key, "T")
        if len(self.d) > self.n:
            self.delete(self.next["H"])
        
    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        val = self.d[key]
        self.delete(key)
        self.add(key, val)
        return val
    
    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.delete(key)
        
        self.add(key, value)
        


## S3:
## https://algo.monster/liteproblems/146        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)