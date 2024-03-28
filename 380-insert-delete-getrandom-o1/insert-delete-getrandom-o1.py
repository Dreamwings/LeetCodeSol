class RandomizedSet:

    def __init__(self):
        self.d = collections.defaultdict(int)
        self.v = []

    def insert(self, val: int) -> bool:
        if val in self.d:
            return False
        self.d[val] = len(self.v)
        self.v.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.d:
            return False
        
        i = self.d[val]
        t = self.v[-1]
        self.v[i] = t
        self.d[t] = i
        self.v.pop()
        del self.d[val]
        return True

    def getRandom(self) -> int:
        
        return random.choice(self.v)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()