from collections import deque
from sortedcontainers import SortedList
from bisect import bisect_left

## S2: See AlgoMonster
## https://algo.monster/liteproblems/1825

## S1: SortedList, Deque, Bisect
## T: O(logM) for add, O(1) for calculate
## S: O(M)

class MKAverage:

    def __init__(self, m: int, k: int):
        self.m, self.k = m, k
        self.q = deque()
        self.sl = SortedList()
        self.total = self.first_k = self.last_k = 0

    def addElement(self, num: int) -> None:
        self.total += num
        self.q.append(num)
        index = self.sl.bisect_left(num)
        if index < self.k:
            self.first_k += num
            if len(self.sl) >= self.k:
                self.first_k -= self.sl[self.k - 1]
                
        if index >= len(self.sl) + 1 - self.k:
            self.last_k += num
            if len(self.sl) >= self.k:
                self.last_k -= self.sl[-self.k]
                
        self.sl.add(num)
        
        if len(self.q) > self.m:
            num = self.q.popleft()
            self.total -= num
            index = self.sl.index(num)
            if index < self.k:
                self.first_k -= num
                self.first_k += self.sl[self.k]
            elif index >= len(self.sl) - self.k:
                self.last_k -= num
                self.last_k += self.sl[-self.k - 1]
            self.sl.remove(num)

    def calculateMKAverage(self) -> int:
        if len(self.sl) < self.m:
            return -1
        return (self.total - self.first_k - self.last_k) // (self.m - 2 * self.k)


        


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()