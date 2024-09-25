def can_steal_all(bags, K, H):
    hours_needed = 0
    for bars in bags:
        # Calculate hours needed for this bag
        hours_needed += (bars + K - 1) // K
    return hours_needed <= H

def minimum_K(N, H, bags):
    left, right = 1, max(bags)
    result = right
    
    while left <= right:
        mid = (left + right) // 2
        
        if can_steal_all(bags, mid, H):
            result = mid  # We can steal all bars with K = mid
            right = mid - 1  # Try for a smaller K
        else:
            left = mid + 1  # Increase K

    return result

# Input reading
N, H = map(int, input().split())
bags = list(map(int, input().split()))

# Output the result
print(minimum_K(N, H, bags))
