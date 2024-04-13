class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        
        ## S1: Hash Table

        # Count the frequency of each remainder when each element in arr is divided by k
        d = Counter(x % k for x in arr)
      
        # Check if the number of elements that are divisible by k is even
        if d[0] % 2 != 0:
            return False
      
        # Check if each non-zero remainder has a complementary count of elements
        # Such that remainder + complementary = k
        # The counts of remainder and its complementary need to be the same
        for remainder in range(1, k):
            if d[remainder] != d[k - remainder]:
                return False
              
        return True