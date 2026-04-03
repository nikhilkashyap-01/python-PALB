def min_swaps(s1, s2):
    if len(s1) != len(s2):
        return -1

    total_ones = s1.count('1') + s2.count('1')

    if total_ones % 2 != 0:
        return -1

    mismatch = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            mismatch += 1

    return mismatch // 2


# Example usage
if __name__ == "__main__":
    s1 = input("Enter first binary string: ")
    s2 = input("Enter second binary string: ")

    result = min_swaps(s1, s2)
    print("Minimum swaps required:", result)