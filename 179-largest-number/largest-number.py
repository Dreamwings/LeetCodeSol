## S2:
## T: O(NlogK), N = len(nums), K is avg length of all str(num)
## S: O(N * K)

class Solution:
    def largestNumber(self, nums):

        if len(nums) == 1:
            return str(nums[0])

        nums_str = list(map(str, nums))
        max_len = max(map(len, nums_str))

        nums_str.sort(key=lambda x: x * (max_len // len(x) + 1), reverse=True)
        # print(nums_str)
        
        return ''.join(nums_str) if int(nums_str[0]) != 0 else '0'



"""
## S1:
## T: O(NlogK), N = len(nums), K is avg length of all str(num)
## S: O(N * K)

class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x
        
class Solution:
    def largestNumber(self, nums):

        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))

        return '0' if largest_num[0] == '0' else largest_num

"""
