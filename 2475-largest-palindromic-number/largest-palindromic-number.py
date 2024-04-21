class Solution:
    def largestPalindromic(self, num: str) -> str:

        from collections import Counter
        
        ## S1: Greedy
        ## T: O(N)
        ## S: O(N)

        # Count the frequency of all digits in num
        # Check how many pair of 9 that we have:
        # If we have one pair of 9, we can make 9XXXXXX9, left = '9' now.
        # If we have two pairs of 9, we can make 99XXXX99, left = '99' now.
        # Continue check pairs for 8,7,6,5,4,3,2,1,0
        # Strip the leading 0 in res
        # Find the maximum digit left that can be used for the middle digit of palindromic number.
        # final result is left + mid + reversed(left)
        # For special input like 00, we need to return 0.

        d = Counter(num)  # str: int, O(N), but there are at most 10 pairs

        left = ''.join(x * (d[x] // 2) for x in '9876543210')  # O(1)
        left = left.lstrip('0')  # Remove leading 0 if there is

        mid = max(x * (d[x] % 2) for x in d)  # O(1)
        # print(mid)
        res = left + mid + left[::-1]

        return res or '0'