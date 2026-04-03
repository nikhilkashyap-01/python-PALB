def election_winner(arr):
    vote_count = {}

    # Step 1: Count votes
    for name in arr:
        vote_count[name] = vote_count.get(name, 0) + 1

    # Step 2: Find winner
    max_votes = 0
    winner = ""

    for name in vote_count:
        if (vote_count[name] > max_votes) or \
           (vote_count[name] == max_votes and name < winner):
            max_votes = vote_count[name]
            winner = name

    return [winner, str(max_votes)]


# Example usage
if __name__ == "__main__":
    arr = input("Enter votes (names separated by space): ").split()
    result = election_winner(arr)
    print("Winner and votes:", result)