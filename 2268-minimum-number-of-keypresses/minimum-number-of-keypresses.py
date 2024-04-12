class Solution:
    def minimumKeypresses(self, s: str) -> int:
        
        ## S1: Greedy
        ## T: O(N + KlogK) ~ O(N) as max K is 26
        ## S: O(26) ~ O(1)

        ch_freq = collections.Counter(s) # O(N) time, result has at most 26 items
        press_times, mapped_cnt, res = 1, 0, 0

        for ch, freq in ch_freq.most_common(): # O(KlogK) for most_common, K <= 26
            mapped_cnt += 1
            res += press_times * freq
            # When mapped 9 or 18 chars, need increment press_times
            if mapped_cnt % 9 == 0:
                press_times += 1

        return res
