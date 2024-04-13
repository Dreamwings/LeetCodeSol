class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        
        ## S1: 
        ## T: O(N^3)
        ## S: O(1)

        max_area = 0
        # Iterate over all possible combinations of three points to form triangles
        for x1, y1 in points:
            for x2, y2 in points:
                for x3, y3 in points:
                    # Calculate vector (u1, v1) from point 1 to point 2
                    u1, v1 = x2 - x1, y2 - y1
                    # Calculate vector (u2, v2) from point 1 to point 3
                    u2, v2 = x3 - x1, y3 - y1
                    # Calculate the triangle's area using the absolute value of the determinant 
                    # (cross product of two vectors) divided by 2
                    area = abs(u1 * v2 - u2 * v1) / 2
                    # Update the max_area if the current area is larger
                    max_area = max(max_area, area)
        
        return max_area

        """
        ## S2:

        return max(0.5 * abs(i[0] * j[1] + j[0] * k[1] + k[0] * i[1]- j[0] * i[1] - k[0] * j[1] - i[0] * k[1])
            for i, j, k in itertools.combinations(p, 3))

        """