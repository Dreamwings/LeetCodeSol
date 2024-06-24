class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        from collections import defaultdict
    
        # Create a dictionary to count the number of roads connected to each city
        d = defaultdict(set)

        for a, b in roads:
            d[a].add(b)
            d[b].add(a)
        
        max_rank = 0

        for i in range(n):
            for j in range(i + 1, n):
                rank = len(d[i]) + len(d[j])
                if j in d[i]:
                    rank -= 1
                max_rank = max(max_rank, rank)
        
        return max_rank
