def missingRange(nums : list[int], lower : int, upper : int) -> list[str]:
    nums.append(upper + 1) #nums = nums + [upper + 1]
    prev = lower - 1
    output = []
    
    for n in nums:
        if n == prev + 2: # n should be prev + 1, if not then it's missing prev + 1.
            output.append(f"{prev + 1}")
        elif n > prev + 2:
            output.append(f"{prev + 1}->{n - 1}")
        prev = n
    return output            
    
nums = [1, 4, 69, 83]
output = missingRange(nums, 0, 100)
print(output)
    
    