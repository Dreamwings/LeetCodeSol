## S1: Sliding Window
## T: O(N), N = len(days), M = avg of days[i]
## S: O(1)

def max_points(days, k):
    def sum_up(n):
        return n * (n + 1) // 2

    # ***** normalize *****
    sum_arr = sum(days)
    score = 0
    for a in days:
        score += sum_up(a)
    
    base_score = k // sum_arr * score
    k = k % sum_arr
    
    if k == 0:
        return base_score
    
    # ***** prepare sliding window *****
    start_sprint = 0
    start_day = 0
    end_sprint = 0
    end_day = 0
    curr_score = 0
    
    while k >= days[end_sprint]:
        curr_score += sum_up(days[end_sprint])
        k -= days[end_sprint]
        end_sprint += 1
    
    curr_score += sum_up(k)
    end_day = k  # exclusive
    best_score = curr_score
    
    # ***** slide the window *****
    while start_sprint < len(days):
        start_days_left = days[start_sprint] - start_day
        end_days_left = days[end_sprint] - end_day
        change = end_day - start_day
        
        if start_days_left == end_days_left:
            curr_score += change * start_days_left
            start_day = 0
            end_day = 0
            start_sprint += 1
            end_sprint = (end_sprint + 1) % len(days)
        elif start_days_left < end_days_left:
            curr_score += change * start_days_left
            start_day = 0
            end_day += start_days_left
            start_sprint += 1
        else:
            curr_score += change * end_days_left
            start_day += end_days_left
            end_day = 0
            end_sprint = (end_sprint + 1) % len(days)
        
        if curr_score > best_score:
            best_score = curr_score
    
    return base_score + best_score


# Example usage:
days = [2, 3, 2]
k = 4
print(max_points(days, k))  # Output should be 8

days = [7, 4, 3, 7, 2]
k = 8
print(max_points(days, k))   # Output should be 32


## =====================================================================

## S2: Sliding Window
## T: O(N*M), N = len(days), M = avg of days[i]
## S: O(N*M)

def max_points(days, k):
    # Generate points for up to the maximum number of days in any sprint
    points = []
    
    # Generate the points array based on days
    for d in days:
        for i in range(1, d + 1):
            points.append(i)
    
    # Use a sliding window to find the maximum sum of k consecutive days
    max_points = win_sum = sum(points[:k])
    m = len(points)
    
    for i in range(k, m * 2):
        i = i % m
        win_sum += points[i] - points[i - k]
        max_points = max(max_points, win_sum)
    
    return max_points



# Example usage:
days = [2, 3, 2]
k = 4
print(max_points(days, k))  # Output should be 8

days = [7, 4, 3, 7, 2]
k = 8
print(max_points(days, k))   # Output should be 32
