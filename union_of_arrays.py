def findUnion(a, b):
    # Convert both arrays to set and take union
    union_set = set(a) | set(b)
    return list(union_set)

if __name__ == "__main__":
    a = [1, 2, 3, 2, 1]
    b = [3, 2, 2, 3, 3, 2]

    result = findUnion(a, b)
    print("Union of arrays:", result)