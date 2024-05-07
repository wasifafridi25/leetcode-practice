def binary_search(nums, target):
    l, r = 0, len(nums) - 1
    
    while ( l <= r):
        
        mid = (l + r) // 2
        
        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
        
        else:
            return mid
    
    return -1

nums = [0, 3, 5, 12, 15]
target = 15
result = binary_search(nums, target)

if result != -1:
    print(f"The target {target} is found at index {result}")   
else:
    print(f"The target {target} is not found in the array")   
                 
    