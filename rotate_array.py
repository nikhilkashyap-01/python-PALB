arr = [1, 2, 3, 4, 5]

# Store last element
last = arr[-1]

# Shift elements to right
for i in range(len(arr)-1, 0, -1):
    arr[i] = arr[i-1]

# Put last element at first position
arr[0] = last

print("Rotated array:", arr)