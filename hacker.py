def getMaxSubarrayLen(team_a, team_b):
    n = len(team_a)

    max_length = 0
    current_length = 1  # Initialize with 1 because each individual hacker is a valid subarray.

    for i in range(1, n):
        if team_a[i] >= team_a[i - 1] and team_b[i] >= team_b[i - 1]:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 1

    max_length = max(max_length, current_length)

    return max_length

# Example usage:
team_a = [2, 7, 3]
team_b = [4, 2, 6]
print(getMaxSubarrayLen(team_a, team_b))  # Output: 3
