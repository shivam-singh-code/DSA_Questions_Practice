# Given an integer array nums, rotate the array to the left by one.

# Note: There is no need to return anything, just modify the given array.


# Examples:
# Input: nums = [1, 2, 3, 4, 5]

# Output: [2, 3, 4, 5, 1]

# Explanation: Initially, nums = [1, 2, 3, 4, 5]

# Rotating once to left -> nums = [2, 3, 4, 5, 1]

# Time complexity O(n)
def left_rotate_by_one(nums):
    temp = nums[0]
    for i in range(1, len(nums)):
        nums[i-1] = nums[i]
    nums[len(nums)-1] = temp
    return nums

print(left_rotate_by_one([1, 2, 3, 4, 5]))