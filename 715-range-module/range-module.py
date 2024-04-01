class RangeModule:

    ## S2: SegmentTree
    ## https://algo.monster/liteproblems/715

    ## S1: Bisect

    from bisect import bisect_left, bisect_right

    def __init__(self):
        self.d = []

    def addRange(self, left: int, right: int) -> None:
        i, j = bisect_left(self.d, left), bisect_right(self.d, right)
        self.d[i:j] = [left]*(i%2 == 0) + [right]*(j%2 == 0)

    def queryRange(self, left: int, right: int) -> bool:
        i, j = bisect_right(self.d, left), bisect_left(self.d, right)
        return i == j and i%2 == 1

    def removeRange(self, left: int, right: int) -> None:
        i, j = bisect_left(self.d, left), bisect_right(self.d, right)
        self.d[i:j] = [left]*(i%2 == 1) + [right]*(j%2 == 1)

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)