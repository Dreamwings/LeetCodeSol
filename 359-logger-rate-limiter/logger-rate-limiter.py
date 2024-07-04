## S1: Hash Table
## T: O(1)
## S: O(M), M is total number of incoming messages

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