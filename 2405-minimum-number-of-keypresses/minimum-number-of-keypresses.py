class Solution:
    def minimumKeypresses(self, s: str) -> int:
        
        ## S1: Greedy

        ch_freq = collections.Counter(s)
        press_times, mapped_cnt, res = 1, 0, 0

        for ch, freq in ch_freq.most_common():
            mapped_cnt += 1
            res += press_times * freq
            # When mapped 9 or 18 chars, need increment press_times
            if mapped_cnt % 9 == 0:
                press_times += 1

        return res
