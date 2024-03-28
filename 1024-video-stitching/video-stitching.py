class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:

        ## S2: DP
        ## https://algo.monster/liteproblems/1024
        ## T: O(N + time)
        ## S: O(time)

        dp = [0] * time
      
        for start, end in clips:
            # Only consider clips that start before the time
            if start < time:
                # Update the dp for the second that this clip starts
                dp[start] = max(dp[start], end)
      
        clips_required = 0  # Counter for the minimum number of clips required
        current_end = 0     # The furthest point we can reach without adding another clip
        next_end = 0        # The furthest point we can reach by including another clip
      
        # Iterate through each second up to the time
        for second in range(time):
            # Determine the most distant point in time we can reach from this second
            next_end = max(next_end, dp[second])
          
            # If the next_end is less or equal to the current second, it means we have a gap.
            # We can't reach the current second from any previous clips.
            if next_end <= second:
                return -1
          
            # When the current second reaches the current_end, we need to select a new clip
            if current_end == second:
                clips_required += 1
                # Update current_end to the furthest point reachable from this clip
                current_end = next_end

        return clips_required

        
        """
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


        ## S3: 
        ## T: O(NlogN)
        ## S: O(1)

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