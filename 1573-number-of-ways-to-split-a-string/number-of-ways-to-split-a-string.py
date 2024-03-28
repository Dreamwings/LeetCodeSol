class Solution:
    def numWays(self, s: str) -> int:
        
        ## S1:

        ones, n, m = s.count('1'), len(s), 10 ** 9 + 7
        if ones == 0:
            return (n - 2) * (n - 1) // 2 % m
        if ones % 3 != 0:
            return 0
            
        ones_in_each_splited_block = ones // 3
        count = ways_of_first_cut = ways_of_second_cut = 0
        for char in s:
            if char == '1':
                count += 1
            if count == ones_in_each_splited_block:
                ways_of_first_cut += 1
            elif count == 2 * ones_in_each_splited_block:
                ways_of_second_cut += 1
        return ways_of_first_cut * ways_of_second_cut % m     

        ## S2: AlgoMonster   