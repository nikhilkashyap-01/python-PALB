def min_time_difference(arr):
    # Convert time to seconds
    times = []
    for t in arr:
        h, m, s = map(int, t.split(':'))
        total_seconds = h * 3600 + m * 60 + s
        times.append(total_seconds)

    # Sort times
    times.sort()

    # Find minimum difference
    min_diff = float('inf')

    for i in range(1, len(times)):
        min_diff = min(min_diff, times[i] - times[i - 1])

    # Check circular difference (midnight wrap)
    seconds_in_day = 24 * 3600
    circular_diff = seconds_in_day - times[-1] + times[0]

    min_diff = min(min_diff, circular_diff)

    return min_diff


# Example usage
if __name__ == "__main__":
    arr = input("Enter time strings separated by space: ").split()
    result = min_time_difference(arr)
    print("Minimum difference in seconds:", result)