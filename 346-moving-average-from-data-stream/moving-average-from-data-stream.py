## S1: Array + Pointers
## T: O(1) for next
## S: O(N)

class MovingAverage:

    def __init__(self, size: int):
        self.n = size        # array size
        self.a = [0] * size
        self.i = 0           # pointer to current pos of the whole data stream
        self.presum = 0      # prefix sum for current window        

    def next(self, val: int) -> float:
        # when self.i >= self.n, left side vals can be overwritten
        # so x = self.i % n
        # need to remove the old val at i from pre_sum
        # cal average with self.n numbers
        # when self.i < self.n, v, cal average with self.i numbers

        k = self.i % self.n
        self.presum += val - self.a[k]
        self.a[k] = val
        self.i += 1

        # need to consider self.i < self.n:
        return 1.0 * self.presum / min(self.i, self.n)
                

## S2: Double-ended Queue
## T: O(1) for next
## S: O(N)

from collections import deque

class MovingAverage:
    def __init__(self, size: int):
        self.n = size
        self.q = deque()
        self.window_sum = 0
        self.count = 0 # number of elements seen so far

    def next(self, val: int) -> float:
        self.count += 1
        # calculate the new sum by shifting the window
        self.q.append(val)
        tail = self.q.popleft() if self.count > self.n else 0

        self.window_sum = self.window_sum - tail + val

        return self.window_sum / min(self.n, self.count)
   


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)