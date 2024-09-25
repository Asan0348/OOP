def can_deliver_with_capacity(children, capacity, flights):
    total_flights = 0
    for c in children:
        total_flights += (c + capacity - 1) // capacity  # equivalent to ceil(c / capacity)
    return total_flights <= flights

def min_capacity(n, f, children):
    left, right = 1, max(children)  # minimum and maximum capacity
    best_capacity = right
    
    while left <= right:
        mid = (left + right) // 2
        if can_deliver_with_capacity(children, mid, f):
            best_capacity = mid
            right = mid - 1  # Try for a smaller capacity
        else:
            left = mid + 1  # Increase capacity
    
    return best_capacity

# Input reading
n, f = map(int, input().split())
children = list(map(int, input().split()))

# Calculate the result
result = min_capacity(n, f, children)

# Output the result
print(result)
