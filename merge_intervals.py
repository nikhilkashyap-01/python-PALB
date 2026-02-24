intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

# Step 1: Sort intervals by start time
intervals.sort()

merged = []

for interval in intervals:
    # If merged list is empty OR no overlap
    if not merged or merged[-1][1] < interval[0]:
        merged.append(interval)
    else:
        # Merge overlapping intervals
        merged[-1][1] = max(merged[-1][1], interval[1])

print("Merged intervals:", merged)