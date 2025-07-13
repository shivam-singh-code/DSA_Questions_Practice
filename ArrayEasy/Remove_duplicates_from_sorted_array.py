# Remove duplicates from sorted array

# Given an integer array nums sorted in non-decreasing order, remove all duplicates in-place so that each unique element appears only once. Return the number of unique elements in the array.
# If the number of unique elements be k, then,

# Change the array nums such that the first k elements of nums contain the unique values in the order that they were present originally.
# The remaining elements, as well as the size of the array does not matter in terms of correctness.


# An array sorted in non-decreasing order is an array where every element to the right of an element is either equal to or greater in value than that element.


# Examples:
# Input: nums = [0, 0, 3, 3, 5, 6]

# Output: 4

# Explanation: Resulting array = [0, 3, 5, 6, _, _]

# There are 4 distinct elements in nums and the elements marked as _ can have any value.


def remove_duplicate(nums):
    unique_element = set()
    for i in range(len(nums)):
        unique_element.add(nums[i])
    for index,element in enumerate(unique_element):
        nums[index] = element
    return len(unique_element)

nums = [0, 0, 3, 3, 5, 6]
# print(remove_duplicate(nums))
# print(nums)

# Time Complexity O(n)
# Space Complexity O(1)
def remove_duplicate_optimal(nums):
    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            nums[i+1] = nums[j]
            i += 1
    return i+1

print(remove_duplicate_optimal(nums))
print(nums)