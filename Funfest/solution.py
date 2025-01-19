def count_events(T, arr):
    # Count how many events can be accessed based on the number of tokens available (T)
    count = 0
    for tokens in arr:
        if tokens <= T:
            count += 1
    return count

# Example usage:
T = int(input())  # The number of tokens Rishith has earned
arr = list(map(int, input().split()))  # The array of tokens required for each event

# Output the number of events Rishith can access
print(count_events(T, arr))
