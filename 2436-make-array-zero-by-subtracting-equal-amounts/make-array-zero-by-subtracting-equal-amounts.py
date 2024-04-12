class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        ## S1:
        ## T: O(N)
        ## S: O(N)

        unique_pos_nums = set([x for x in nums if x])
        return len(unique_pos_nums)