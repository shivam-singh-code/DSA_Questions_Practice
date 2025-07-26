# Given an array of integers nums and an integer target. Return the indices(0 - indexed) of two elements in nums such that they add up to target.



# Each input will have exactly one solution, and the same element cannot be used twice. Return the answer in non-decreasing order.


# Examples:
# Input: nums = [1, 6, 2, 10, 3], target = 7

# Output: [0, 1]

# Explanation: nums[0] + nums[1] = 1 + 6 = 7


# Time complexity is o(n^2) and space O(1)
def two_sum_brute(nums, target):
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            if nums[i] + nums[j] == target:
                return i, j
    return False

# print(two_sum_brute([1, 6, 2, 10, 3], 7))
# print(two_sum_brute([1, 3, 5, -7, 6, -3], 0))


# Time complexity is o(n) and space O(n)
def two_sum_better(nums, target):
    hash_map = {}
    for index, number in enumerate(nums):
        difference = target - number
        if difference in hash_map:
            return sorted([hash_map[difference], index]) #O(1) due to two elements
        hash_map[number] = index


# Time complexity is O(n log n) and space O(1)
def two_sum_optimal(nums, target):
    nums.sort()
    left, right = 0, len(nums) - 1
    while left < right:
        Sum = nums[left] + nums[right]
        if Sum == target :
            return left, right
        elif Sum > target:
            right -= 1
        else:
            left += 1



# print(two_sum_better([1, 6, 2, 10, 3], 7))
# print(two_sum_better([1, 3, 5, -7, 6, -3], 0))
            
print(two_sum_optimal([1, 6, 2, 10, 3], 7))
print(two_sum_optimal([1, 3, 5, -7, 6, -3], 0))
