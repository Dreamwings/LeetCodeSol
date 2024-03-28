class Solution:
    def isHappy(self, n: int) -> bool:
        
        ## S1: Hashset

        seen = set()
        
        while n not in seen:
            seen.add(n)
            n = sum(int(i) ** 2 for i in str(n))
        
        # while loop will break when n is already in seen and there will be a loop        
        return n == 1

        """
        ## S2: See AlgoMonster
        ## T: O(logN)
        ## S: O(1)

        def get_next_number(x):
            total_sum = 0
            # Continue until x is reduced to zero
            while x:
                # Divide x by 10, saving the remainder and the quotient
                x, digit = divmod(x, 10)
                # Add the square of the remainder to total_sum
                total_sum += digit * digit
            return total_sum

        # Initialize two pointers for detecting cycles (Floyd's cycle detection algorithm)
        slow = n
        fast = get_next_number(n)
      
        # Loop until the two pointers meet or we find a happy number
        while slow != fast:
            # The slow pointer moves one step at a time
            slow = get_next_number(slow)
            # The fast pointer moves two steps at a time
            fast = get_next_number(get_next_number(fast))
      
        # The number is happy if and only if the loop ends with slow equals to 1
        return slow == 1
        """