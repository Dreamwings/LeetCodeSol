class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:

        ## S1: Sorting
        ## T: O(NlogN)
        ## S: O(1)

        end, end2, res = -1, 0, 0
        for i, j in sorted(clips):
            if end2 >= time or i > end2:
                break
            elif end < i <= end2 and j > end2:
                res, end = res + 1, end2
            end2 = max(end2, j)
        return res if end2 >= time else -1        

        """
        ## S2: DP

        dp = [float('inf')] * (time + 1)
        dp[0] = 0
        for i in range(1, time + 1):
            for start, end in clips:
                if start <= i <= end:
                    dp[i] = min(dp[start] + 1, dp[i])
        if dp[time] == float('inf'):
            return -1
        return dp[time]
        
        
        ## S3: 



        clips.sort(key = lambda x: (x[0],-x[1]))
        t, cSet, ans = 0, set(), 0

        while clips:
            while clips and clips[0][1] <= t: clips.pop(0)
            while clips and clips[0][0] <= t: cSet.add(clips.pop(0)[1])

            if clips and not cSet: return -1
            t = max(cSet) if cSet else t
            ans+= 1
            if t >= time: return ans 
            cSet.clear()

        return -1     

        """   