
def kthSmallest(arr, k):
    arr.sort()
    return arr[k - 1]

if __name__ == "__main__":
    arr = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
    k = 4
    result = kthSmallest(arr, k)
    print("Kth smallest element is:", result)