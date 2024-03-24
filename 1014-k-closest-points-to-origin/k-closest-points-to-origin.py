class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        from heapq import nsmallest, heappush, heappop
                
        ## S1: Optimal
        ## Time: O(N*logK)
        ## Space: O(N)
        
        closest = nsmallest(K, [(x*x + y*y, x, y) for x, y in points])
        
        return [[x, y] for d, x, y in closest]

        """
        ## S2:
        ## Time: O(N*logK)
        ## Space: O(N)

        hq = []
        
        for x, y in points:
            heappush(hq, (-x*x-y*y, x, y))
            if len(hq) > K:
                heappop(hq)
        
        return [(x, y) for _, x, y in hq]


        ## S3: Sort
        ## Time: O(N*logN)
        ## Space: O(N)        

        points.sort(key=lambda point: point[0]**2 + point[1]**2)
        return points[:K]

        """