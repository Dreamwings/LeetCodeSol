class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        ## S1:

        return nums * 2

        
        ## S2:
        
        nums.extend(nums)
        return nums