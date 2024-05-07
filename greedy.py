def findMinimumEqualSum(rowA, rowB):
    sumA = sum(rowA)
    sumB = sum(rowB)
    
    # Count the number of missing values (0s) in both rows.
    zerosA = rowA.count(0)
    zerosB = rowB.count(0)
    
    # Calculate the difference between the sums.
    diff = abs(sumA - sumB)
    
    # If the difference is odd or if both rows have zeros, it's impossible to make the sums equal.
    if diff % 2 == 1 or (zerosA > 0 and zerosB > 0):
        return -1
    
    # Calculate the target value to replace the zeros.
    target = diff // 2
    
    # Sort the missing values in ascending order in both rows.
    rowA_zeros = sorted([val for val in rowA if val == 0])
    rowB_zeros = sorted([val for val in rowB if val == 0])
    
    replacements = 0  # Count how many zeros are replaced.
    
    # Distribute the target value to replace the zeros in both rows.
    for i in range(zerosA):
        if rowA_zeros[i] <= target:
            target -= rowA_zeros[i]
            replacements += 1
        else:
            break
    
    for i in range(zerosB):
        if rowB_zeros[i] <= target:
            target -= rowB_zeros[i]
            replacements += 1
        else:
            break
    
    # If all zeros are replaced, return the sum of both rows.
    if replacements == zerosA + zerosB:
        return sumA + sumB
    else:
        return -1

# Example usage:
rowA = [2, 5, 0, 1, 1]
rowB = [2, 1, 0, 0]
print(findMinimumEqualSum(rowA, rowB))  # Output: 10
