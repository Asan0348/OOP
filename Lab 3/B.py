def can_partition(houses, n, k, max_ghouls):
    current_sum = 0
    blocks_used = 1  # Start with the first block

    for i in range(n):
        current_sum += houses[i]

        # If adding the current house exceeds max_ghouls, we need a new block
        if current_sum > max_ghouls:
            blocks_used += 1  # Use a new block
            current_sum = houses[i]  # Start the new block with the current house

            # If we exceed the number of blocks allowed, return False
            if blocks_used > k:
                return False

    return True  # Successfully partitioned into k or fewer blocks

def min_max_ghouls(n, k, houses):
    low = max(houses)  # Lower bound
    high = sum(houses)  # Upper bound
    answer = high  # Initialize answer to maximum possible

    # Perform binary search
    while low <= high:
        mid = low + (high - low) // 2

        # Check if it's possible to partition
        if can_partition(houses, n, k, mid):
            answer = mid  # If yes, update answer and try for smaller
            high = mid - 1
        else:
            low = mid + 1  # Otherwise, try a larger max

    return answer

# Input reading
n, k = map(int, input().split())
houses = list(map(int, input().split()))

# Calculate and output the result
result = min_max_ghouls(n, k, houses)
print(result)
