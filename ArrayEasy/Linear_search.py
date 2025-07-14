# Given an array of integers nums and an integer target, find the smallest index (0 based indexing) where the target appears in the array. If the target is not found in the array, return -1


# Examples:
# Input: nums = [2, 3, 4, 5, 3], target = 3

# Output: 1

# Explanation: The first occurence of 3 in nums is at index 1


def linear_search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    
    return -1


print(linear_search([2, 3, 4, 5, 3], 3))
