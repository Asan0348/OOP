def min_square_side_to_catch_sheep(N, K, pastures):
    # Calculate the required square side for each sheep's pasture
    required_sizes = []
    for pasture in pastures:
        x1, y1, x2, y2 = pasture
        # The size needed to cover this pasture is the max of the top-right corner
        required_size = max(x2, y2)
        required_sizes.append(required_size)
    
    # Sort the required sizes
    required_sizes.sort()
    
    # The minimum length of the square paddock to cover at least K pastures
    # is the K-th smallest size (1-indexed, so we access K-1 in 0-indexed list)
    return required_sizes[K-1]

# Input reading
N, K = map(int, input().split())
pastures = []
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    pastures.append((x1, y1, x2, y2))

# Calculate and print the result
result = min_square_side_to_catch_sheep(N, K, pastures)
print(result)
