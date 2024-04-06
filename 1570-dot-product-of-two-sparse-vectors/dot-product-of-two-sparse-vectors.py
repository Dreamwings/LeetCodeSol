class SparseVector:
    def __init__(self, nums: List[int]):
        self.sparse_vec = {i: v for i, v in enumerate(nums) if v != 0}        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        a, b = self.sparse_vec, vec.sparse_vec
        if len(a) > len(b):
            a, b = b, a
        # return sum(a[i] * b[i] for i in a if i in b)
        return sum(a[i] * b.get(i, 0) for i in a)

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
