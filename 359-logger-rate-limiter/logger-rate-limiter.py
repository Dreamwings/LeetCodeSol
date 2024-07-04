from collections import deque

## S3: Two Hash Tables (Optimal)
## T: O(1)
## S: O(N), N is num of msg in 20s

class Logger:

    def __init__(self):
        # Two dictionaries
        self.old = {}
        self.new = {}
        # Keeps track of the timestamp of the first message we added in either of the dictionaries.
        self.last_ts = 0
        
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # If the current message is 20 seconds greater than the first message seen in self.old.
        if timestamp >= self.last_ts + 20:
            self.old.clear()
            self.new.clear()
            self.last_ts = timestamp
        # If the current message is 10 seconds greater than the first message seen in self.new.
        elif timestamp >= self.last_ts + 10:
            self.old = self.new
            self.new = {}
            self.last_ts = timestamp
        
        if message in self.new:
            return False
        if message in self.old and timestamp < self.old.get(message) + 10:
            return False
        self.new[message] = timestamp
        return True



## S2: Queue + Hash Set
## T: O(N), N is num of msg in 10s
## S: O(N)
## Problem: One downside is that if many unique messages are received in the 10 second window (say 1 million), the Queue can become very large. When it comes time to cleanup the Queue, the method will spend a lot time polling all messages off the Queue before returning. So in this example a lookuo that should be O(1) could be as bad as O(n) (where n is the number of records received, if we received 1 million records in the first 10 seconds)

class Logger:

    def __init__(self):
        
        self.q = deque()
        self.set = set()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:

        while self.q:
            msg, ts = self.q[0]
            if timestamp - ts >= 10: # Only keeps msg in 10s
                self.q.popleft()
                self.set.remove(msg)
            else:
                break
        
        if message not in self.set:
            self.set.add(message)
            self.q.append((message, timestamp))
            return True
        else:
            return False


## S1: Hash Table
## T: O(1)
## S: O(M), M is total number of incoming messages
## Problem: Memory usage grows continuously.

class Logger:

    def __init__(self):
        
        self.last_msg = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:

        if message in self.last_msg and timestamp - self.last_msg[message] < 10:
            return False

        self.last_msg[message] = timestamp
        return True

## S4: Thread Safe Solution
## It's possible that the Logger is called with the same message at the same time from multiple sources. In that case the HashMap might not have been updated fast enough when the second duplicate message arrives.

# For example:
# New message m1 arrives at time 1
# Same message m1 arrives again at time 1
# Logger is called with (m1, 1)
# Logger is called with (m1, 1)
# The second call will possibly print the message if the first call (#3) hasn't had a chance to create the HashMap entry for m1 yet.
# One possible solution is to use a lock

from multiprocessing import Semaphore

class Logger:
    def __init__(self):
        # message to last time seen
        # python dict is thread-safe
        self.m = {}
        self.lock = Semaphore(1)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        self.lock.acquire()
        m = self.m
        if message not in m or timestamp - m[message] >= 10:
            m[message] = timestamp
            self.lock.release()
            return True

        self.lock.release()
        return False



# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)