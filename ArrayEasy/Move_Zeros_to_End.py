# Given an integer array nums, move all the 0's to the end of the array. The relative order of the other elements must remain the same. This must be done in place, without making a copy of the array.


# Examples:
# Input: nums = [0, 1, 4, 0, 5, 2]

# Output: [1, 4, 5, 2, 0, 0]

# Explanation: Both the zeroes are moved to the end and the order of the other elements stay the same

# Time complexity O(n)
# Space Complexity O(1)
def move_zeros(nums):
    j = -1
    for i in range(len(nums)):
        if nums[i] == 0:
            j = i
            break
    
    if j == -1:
        return nums
    
    for i in range(j+1, len(nums)):
        if nums[i] != 0:
            swap(nums, i, j)
            j += 1
    
    return nums

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

print(move_zeros([0, 1, 4, 0, 5, 2]))