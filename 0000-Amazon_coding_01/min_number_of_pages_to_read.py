def minimumNumberOfPages(pages, days):

    ## S1: Binary Search
    ## T: O(logN)
    ## S: O(1)
    
    def can_read(pages, days, x):
        cnt = 0
        
        for p in pages:
            cnt += (p - 1) // x + 1
            # if p <= x:
            #     cnt += 1
            # else:
            #     cnt += (p - 1) // x + 1
        
        return cnt <= days
    
    lo, hi = 1, max(pages)
    res = -1
    
    while lo <= hi:
        mid = (lo + hi) // 2
        if can_read(pages, days, mid):
            res = mid
            hi = mid - 1
        else:
            lo = mid + 1
    
    return res
                

pages = [2, 4, 3]
days = 4
res = minimumNumberOfPages(pages, days)
print(res)
