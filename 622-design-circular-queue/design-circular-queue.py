## S2: Linked List
## https://leetcode.com/problems/design-circular-queue/editorial/

## S1: Array

class MyCircularQueue:
    def __init__(self, k: int):
        self.queue = [0] * k  # Initialize the circular queue with 'k' elements set to 0
        self.head_index = 0  # The front pointer to the first element of the circular queue
        self.count = 0  # Current number of elements in the circular queue
        self.capacity = k  # Maximum capacity of the circular queue

    def enQueue(self, value: int) -> bool:
        """Inserts an element into the circular queue. Return true if the operation is successful."""
        if self.isFull():
            # Return False if the queue is full
            return False
        # Calculate the index at which to insert the new value
        idx = (self.head_index + self.count) % self.capacity
        self.queue[idx] = value  # Insert the value
        self.count += 1  # Increment the size of the queue
        return True  # Return True on successful insertion

    def deQueue(self) -> bool:
        """Deletes an element from the circular queue. Return true if the operation is successful."""
        if self.isEmpty():
            # Return False if the queue is empty
            return False
        # Increment the head_index as we remove the front element
        self.head_index = (self.head_index + 1) % self.capacity
        self.count -= 1  # Decrement the size of the queue
        return True  # Return True on successful deletion

    def Front(self) -> int:
        """Gets the front item from the queue. If the queue is empty, return -1."""
        if self.isEmpty():
            # If the queue is empty, return -1
            return -1
        # Otherwise, return the front element
        return self.queue[self.head_index]

    def Rear(self) -> int:
        """Gets the last item from the queue. If the queue is empty, return -1."""
        if self.isEmpty():
            # If the queue is empty, return -1
            return -1
        # Calculate the index of the rear element
        idx = (self.head_index + self.count - 1) % self.capacity
        # Return the rear element
        return self.queue[idx]

    def isEmpty(self) -> bool:
        """Checks whether the circular queue is empty."""
        # Return True if count equals 0, meaning the queue is empty
        return self.count == 0

    def isFull(self) -> bool:
        """Checks whether the circular queue is full."""
        # Return True if count equals the capacity, meaning the queue is full
        return self.count == self.capacity
 


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()