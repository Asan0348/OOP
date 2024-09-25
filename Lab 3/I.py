def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Check if x is present at mid
        if arr[mid] == x:
            return "Yes"
        # If x is greater, ignore the left half
        elif arr[mid] < x:
            left = mid + 1
        # If x is smaller, ignore the right half
        else:
            right = mid - 1
    
    return "No"

# Input reading
n = int(input())
arr = list(map(int, input().split()))
x = int(input())

# Output result
print(binary_search(arr, x))
