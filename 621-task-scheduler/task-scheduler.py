class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        ## S1:

        from collections import Counter
        
        d = Counter(tasks)
        M = max(d.values())
        num = 0  # num of tasks which have the max freq
        for k, v in d.items():
            if v == M:
                num += 1
        
        # we only need to consider those max num tasks
        # e.g: A, B, C, D, E
        # A, C, E has the max num tasks, M times
        # Case 1: if n <= num, say n = 2, num = 4, it can always be something like
        # ACE*ACE*ACE*ACE, * places can have B or D or both
        # in this case, no empty time units are necessary, the max time will be: len(tasks)
        # Case 2: if n > num, say n = 6, num = 4, say A, C, E each 4 times, B 2 times, D 1 time
        # ACEBD..ACEB...ACE....ACE
        # in this case, need to consider empty time, we have (M - 1) gaps to fill between first A and last A
        # and there are the last cycle A, C and E
        # so (M - 1) * (n + 1) + num, which is larger than len(tasks)
        
        # as a result, the total time will be the larger of the two cases
        x = len(tasks) # when M is small compared with x, there are many different tasks, meet n easily
        y = (M - 1) * (n + 1) + num # M is large, need to add idle periods
        
        return max(x, y)