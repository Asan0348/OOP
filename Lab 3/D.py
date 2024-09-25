import bisect

def solve_queries(n, q, a, queries):
    # Sort the array for binary search
    a.sort()
    results = []
    
    for l1, r1, l2, r2 in queries:
        # Count of elements in (l1, r1) which means strictly between l1 and r1
        count1 = bisect.bisect_right(a, r1) - bisect.bisect_left(a, l1)
        
        # Count of elements in [l2, r2] which means inclusive
        count2 = bisect.bisect_right(a, r2) - bisect.bisect_left(a, l2)
        
        # Find overlap count: we need to find elements that are in both ranges
        overlap_count = 0
        
        # To find the overlap:
        # We are interested in the range that satisfies both conditions:
        # l1 < a < r1 AND l2 <= a <= r2
        # This implies:
        # 1. Start of overlap: max(l1, l2)
        # 2. End of overlap: min(r1, r2)
        overlap_start = max(l1, l2)
        overlap_end = min(r1, r2)
        
        # Check if there is a valid overlap
        if overlap_start < overlap_end:
            overlap_count = bisect.bisect_right(a, overlap_end) - bisect.bisect_left(a, overlap_start)
        
        # Total count is the sum of both counts minus overlap
        total_count = count1 + count2 - overlap_count
        
        results.append(total_count)
    
    return results

# Read input
n, q = map(int, input().split())
a = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(q)]

# Get results
results = solve_queries(n, q, a, queries)

# Print output
for result in results:
    print(result)
