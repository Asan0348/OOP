def min_subarray_length(n, k, arr):
    start = 0
    current_sum = 0
    min_length = float('inf')  # Use infinity as the initial value for minimum length
    
    for end in range(n):
        current_sum += arr[end]  # Expand the window by including arr[end]
        
        # Try to shrink the window as long as the condition is satisfied
        while current_sum >= k:
            min_length = min(min_length, end - start + 1)  # Update the minimum length
            current_sum -= arr[start]  # Shrink the window from the left
            start += 1  # Move the start pointer right
            
    return min_length

# Input reading
n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Output the result
print(min_subarray_length(n, k, arr))
