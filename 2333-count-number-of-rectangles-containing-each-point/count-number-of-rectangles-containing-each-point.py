class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        
        ## S1: Binary Search
        ## T: O((N + M)*logN), N = len(rectangles), M = len(points)
        ## S: O(N)

        # Create a dictionary to store the x-coordinates grouped by their y-coordinates.
        dict_y_x = defaultdict(list) # y: [x1, x2,...]
      
        # Go through each rectangle and group x-coordinates by y.
        for x, y in rectangles:
            dict_y_x[y].append(x)
          
        # Sort each list of x-coordinates for binary search efficiency.
        for yval in dict_y_x.values():
            yval.sort()
          
        res = []
      
        # For each point, count the number of rectangles that can cover it.
        for x, y in points:
            count = 0
            # Check each possible y-coordinate (height) at or above the point's y.
            for h in range(y, 101):
                # Retrieve the list of x-coordinates at the current height.
                x_at_h = dict_y_x[h]
                # Use binary search to find the starting position where 
                # rectangles at this height can cover the point.
                count += len(x_at_h) - bisect_left(x_at_h, x)
            # Append the count to res list for the current point.
            res.append(count)
      
        return res
