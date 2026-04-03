def min_add_to_make_valid(s):
    balance = 0       # unmatched '('
    open_needed = 0   # needed '('

    for ch in s:
        if ch == '(':
            balance += 1
        else:  # ch == ')'
            if balance > 0:
                balance -= 1
            else:
                open_needed += 1

    # balance = extra '(' → need same number of ')'
    return open_needed + balance


# Example usage
if __name__ == "__main__":
    s = input("Enter parentheses string: ")
    result = min_add_to_make_valid(s)
    print("Minimum additions required:", result)