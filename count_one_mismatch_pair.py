def count_pairs(arr):
    n = len(arr)
    count = 0

    # Compare every pair
    for i in range(n):
        for j in range(i + 1, n):
            diff = 0

            # Compare characters
            for k in range(len(arr[i])):
                if arr[i][k] != arr[j][k]:
                    diff += 1
                if diff > 1:
                    break

            if diff == 1:
                count += 1

    return count


# Example usage
if __name__ == "__main__":
    arr = input("Enter strings separated by space: ").split()
    result = count_pairs(arr)
    print("Number of valid pairs:", result)