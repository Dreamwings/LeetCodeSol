from collections import deque

## S2: Queue + Hash Set
## T: O(N), N is num of msg in 10s
## S: O(N)

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
## Problem: It's possible that the Logger is called with the same message at the same time from multiple sources. In that case the HashMap might not have been updated fast enough when the second duplicate message arrives.

# For example:
# New message m1 arrives at time 1
# Same message m1 arrives again at time 1
# Logger is called with (m1, 1)
# Logger is called with (m1, 1)
# The second call will possibly print the message if the first call (#3) hasn't had a chance to create the HashMap entry for m1 yet.
# One possible solution is to use a lock

class Logger:

    def __init__(self):
        
        self.last_msg = dict()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:

        if message in self.last_msg and timestamp - self.last_msg[message] < 10:
            return False

        self.last_msg[message] = timestamp
        return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)