class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:

        ## S2: Graham Scan
        ## https://leetcode.com/problems/erect-the-fence/solutions/1442266/a-detailed-explanation-with-diagrams-graham-scan/
        ## T: O(NlogN)
        ## S: O(N)

        def cmp(p1, p2, p3):
            x1, y1 = p1
            x2, y2 = p2            
            x3, y3 = p3
            
            return (y3 - y2) * (x2 - x1) - (y2 - y1) * (x3 - x2)
        
        points = sorted(trees)
        
        lower = []
        upper = []
        for point in points:
            while len(lower) >= 2 and cmp(lower[-2], lower[-1], point) < 0:
                lower.pop()
            while len(upper) >= 2 and cmp(upper[-2], upper[-1], point) > 0:
                upper.pop()
            
            lower.append(tuple(point))
            upper.append(tuple(point))
        
        return list(set(lower+upper))


        """
        ## S1: Jarvis’s Algorithm (a.k.a. the Gift Wrapping algorithm)
        ## T: O(NlogN)
        ## S: O(N)

        # Function to calculate the cross product of vectors AB and BC. 
        # This helps determine the orientation of the triplet (A, B, C).
        def cross_product(A_idx, B_idx, C_idx):
            A, B, C = points[A_idx], points[B_idx], points[C_idx]
            return (B[0] - A[0]) * (C[1] - B[1]) - (B[1] - A[1]) * (C[0] - B[0])

        n = len(points)
        # If there are less than 4 points, all of them constitute the convex hull.
        if n < 4:
            return points

        # Sort points by their x-coordinate, and in case of a tie, by their y-coordinate.
        points.sort()
        # Initialize a visited array to track points that are part of the convex hull.
        visited = [False] * n
        # Initialize a stack to maintain the points forming the hull.
        stack = [0]
        # Construct the lower hull by moving left to right.
        for i in range(1, n):
            # While there are at least two points and the sequence forms a non-left turn, remove the middle point.
            while len(stack) > 1 and cross_product(stack[-2], stack[-1], i) < 0:
                visited[stack.pop()] = False
            visited[i] = True
            stack.append(i)
      
        # Remember the size of the stack to differentiate the lower and upper hull.
        lower_hull_size = len(stack)
        # Construct the upper hull by moving right to left.
        for i in range(n - 2, -1, -1):
            # Skip the point if it's already in the stack.
            if visited[i]:
                continue
            # Similar to the lower hull construction but adding from the upper side.
            while len(stack) > lower_hull_size and cross_product(stack[-2], stack[-1], i) < 0:
                stack.pop()
            stack.append(i)
      
        # Remove the last point because it's the same as the first one in the stack.
        stack.pop()
        # Construct and return the list of points that form the outer trees (convex hull).
        return [points[i] for i in stack]

        """
