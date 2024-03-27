class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        ## S1
        ## Time: O(N)
        ## Space: O(N)

        # Example: intLength = 8, n = 3
        # 1: 1000 ----------> Palindrome = 1000 + 0001 = 10000001
        # 2: 1001 ----------> Palindrome = 1001 + 1001 = 10011001
        # 3: 1002 ----------> Palindrome = 1002 + 2001 = 10022001
        # ......
        # 100: 1099 ----------> Palindrome = 1099 + 9901 = 10999901
        # Example: intLength = 5, n = 2
        # 1: 100 ----------> Palindrome = 100 | 001 = 10001
        # 2: 101 ----------> Palindrome = 101 | 101 = 10101
        # 3: 102 ----------> Palindrome = 102 | 201 = 10201

        n = (intLength + 1) // 2 - 1   # half length of palindrome numbers
        res, s = [], ''
        
        for i in queries:
            x = str(10 ** n + i - 1)
            if intLength & 1: # Odd
                s = x + x[::-1][1:]
            else: # Even
                s = x + x[::-1]
            res.append(int(s) if len(s) == intLength else -1)

        return res
