def two_sum(nums, target):
    num_indices = {}  # Hashmap to store num:index pairs
    
    for i, num in enumerate(nums):
        diff = target - num
        if diff in num_indices:
            return [num_indices[diff], i]
        num_indices[num] = i
    
    # If no solution is found
    return []

# Example usage:
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # Output: [0, 1]
