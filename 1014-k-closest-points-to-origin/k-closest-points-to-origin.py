class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        from heapq import nsmallest, heappush, heappop

        ## S5: Quick Select Sorting, Divide and Conquer (Optimal)
        ## Time: O(N) on avg, O(N^2) for worst case
        ## Space: O(N)

        dist_sq = lambda x, y: x*x + y*y

        # compute distance square for all points
        dist_xy = [(dist_sq(x, y), x, y) for x, y in points]  # O(N)

        def quick_select_sort(dist_xy, K):
            pivot = random.choice(dist_xy)[0]  # Choose a dist_xy randomly
            # Initialize 3 arrays to hold points for dist_xy < pivot, dist_xy == pivot, dist_xy > pivot respectively
            sm, eq, gt = [], [], []

            for v in dist_xy:  # v is (distance, x, y)
                if v[0] < pivot:
                    sm.append(v)
                elif v[0] > pivot:
                    gt.append(v)
                else:
                    eq.append(v)

            len_sm, len_eq = len(sm), len(eq)
            if K <= len_sm:  # Note here "=" is important
                return quick_select_sort(sm, K)
            elif K > len_sm + len_eq:
                return sm + eq + quick_select_sort(gt, K - len_sm - len_eq)
            else:
                return sm + eq

        k_smallest = quick_select_sort(dist_xy, K)

        return [[x, y] for _, x, y in k_smallest]



        ## S1: Optimal
        ## Time: O(N*logK)
        ## Space: O(N)
        
        closest = nsmallest(K, [(x*x + y*y, x, y) for x, y in points])
        
        return [[x, y] for d, x, y in closest]



        ## S2: Max Heap
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



        ## S4: Optimal, Divide and Conquer
        ## Time: O(N) on avg, O(N^2) for worst case
        ## Space: O(N)

        # Idea: Sort partially the distance so that the first K elem are the smallest

        dist = lambda i: points[i][0]**2 + points[i][1]**2

        def partition(i, j):
            # Partition by pivot A[i], returning an index mid
            # such that A[i] <= A[mid] <= A[j] for i < mid < j.
            idx = i
            pivot = dist(i)
            i += 1

            while True:
                while i < j and dist(i) < pivot:
                    i += 1
                while i <= j and dist(j) >= pivot:
                    j -= 1
                if i >= j: break
                points[i], points[j] = points[j], points[i]

            points[idx], points[j] = points[j], points[idx]
            return j
        
        def quick_select_sort(i, j, K):
            # Partially sorts A[i:j+1] so the first K elements are
            # the smallest K elements.
            if i >= j: return

            # Put random element as A[i] - this is the pivot
            v = random.randint(i, j)
            points[i], points[v] = points[v], points[i]

            mid = partition(i, j)
            if mid == K:
                return
            elif K < mid - i + 1:
                quick_select_sort(i, mid - 1, K)
            elif K > mid - i + 1:
                quick_select_sort(mid + 1, j, K - (mid - i + 1))


        quick_select_sort(0, len(points) - 1, K)
        return points[:K]

