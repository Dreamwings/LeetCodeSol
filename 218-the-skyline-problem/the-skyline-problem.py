class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        
        ## S1: Priority Queue and Sweeping Line
        ## T: O(NlogN)
        ## S: O(N)

        # Iterate over all buildings, for each building i,
        # add (position, i) to edges.
        edges = []
        for i, (l, r, h) in enumerate(buildings):
            edges.append([l, i])
            edges.append([r, i])

        # Sort edges by non-decreasing order.
        edges.sort()
     
        # Initailize an empty Priority Queue 'pq' to store all the 
        # newly added buildings, an empty list res to store the skyline key points.
        n, pq, res, i = len(edges), [], [], 0
        
        # Iterate over all the sorted edges.
        while i < n:
            
            # Since we might have multiple edges at same x,
            # Let the 'x' be the current position along the x-axis.
            x = edges[i][0]
            
            # While we are handling the edges at 'x':
            while i < n and edges[i][0] == x:
                # The index 'j' of this building in 'buildings'
                j = edges[i][1]
                
                # If this is a left edge of building 'j', we
                # add (height, r_edge) of building 'j' to 'pq'.
                if buildings[j][0] == x:
                    r_edge = buildings[j][1]
                    height = buildings[j][2]
                    heapq.heappush(pq, [-height, r_edge])
                    
                # If the tallest pq building has been passed,
                # we remove it from 'pq'.
                while pq and pq[0][1] <= x:
                    heapq.heappop(pq)
                
                i += 1
            
            # Get the maximum height from 'pq'.
            max_height = -pq[0][0] if pq else 0
            
            # If the height changes at this x, we add this
            # skyline key point [x, max_height] to 'res'.
            if not res or max_height != res[-1][1]:
                res.append([x, max_height])
        
        return res
