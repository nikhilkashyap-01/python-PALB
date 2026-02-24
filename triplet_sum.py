arr = [1, 4, 45, 6, 10, 8]
target = 13

arr.sort()
n = len(arr)
found = False

for i in range(n - 2):
    left = i + 1
    right = n - 1

    while left < right:
        current_sum = arr[i] + arr[left] + arr[right]

        if current_sum == target:
            found = True
            break
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    if found:
        break

print(found)