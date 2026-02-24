a = [2, 4, 7, 10]
b = [2, 3]

n = len(a)
m = len(b)

# Function to calculate next gap
def nextGap(gap):
    if gap <= 1:
        return 0
    return (gap // 2) + (gap % 2)

gap = nextGap(n + m)

while gap > 0:
    i = 0

    # Compare elements in first array
    while i + gap < n:
        if a[i] > a[i + gap]:
            a[i], a[i + gap] = a[i + gap], a[i]
        i += 1

    # Compare elements between arrays
    j = gap - n if gap > n else 0
    while i < n and j < m:
        if a[i] > b[j]:
            a[i], b[j] = b[j], a[i]
        i += 1
        j += 1

    # Compare elements in second array
    if j < m:
        j = 0
        while j + gap < m:
            if b[j] > b[j + gap]:
                b[j], b[j + gap] = b[j + gap], b[j]
            j += 1

    gap = nextGap(gap)

print("a[] =", a)
print("b[] =", b)