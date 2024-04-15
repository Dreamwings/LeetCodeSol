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
        # can also use move_to_end method
        # self.d.move_to_end(key)
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            del self.d[key]
            # can also use move_to_end method
            # self.d.move_to_end(key)

        self.d[key] = value
        if len(self.d) > self.n:
            self.d.popitem(last=False)



## S3: Double Linked List
## T: O(1) for get and put
## S: O(N)

class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, node):
        previous_end = self.tail.prev
        previous_end.next = node
        node.prev = previous_end
        node.next = self.tail
        self.tail.prev = node
        
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        
        node = self.dic[key]
        self.remove(node)
        self.add(node)
        return node.val
        
    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            old_node = self.dic[key]
            self.remove(old_node)
        
        node = ListNode(key, value)
        self.dic[key] = node
        self.add(node)
        
        if len(self.dic) > self.capacity:
            node_to_delete = self.head.next
            self.remove(node_to_delete)
            del self.dic[node_to_delete.key]




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
        

## S4: Double Linked List (https://algo.monster/liteproblems/146)
## T: O(1) for get and put
## S: O(N)
##  


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)