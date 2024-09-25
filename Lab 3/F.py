from bisect import bisect_right

def mark_competitors(N, competitors, P, rounds):
    # Sort the competitors' powers
    competitors.sort()
    
    # Create a prefix sum array
    prefix_sum = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix_sum[i] = prefix_sum[i - 1] + competitors[i - 1]
    
    results = []
    
    for power in rounds:
        # Find how many competitors have power less than or equal to Mark's power
        count = bisect_right(competitors, power)
        total_power = prefix_sum[count]
        results.append((count, total_power))
    
    return results

# Input reading
N = int(input())
competitors = list(map(int, input().split()))
P = int(input())
rounds = [int(input()) for _ in range(P)]

# Process the results
results = mark_competitors(N, competitors, P, rounds)

# Output the results
for count, total_power in results:
    print(count, total_power)
