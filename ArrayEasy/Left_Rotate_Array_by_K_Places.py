# Given an integer array nums and a non-negative integer k, rotate the array to the left by k steps.


# Examples:
# Input: nums = [1, 2, 3, 4, 5, 6], k = 2

# Output: nums = [3, 4, 5, 6, 1, 2]

# Explanation: rotate 1 step to the left: [2, 3, 4, 5, 6, 1]

# rotate 2 steps to the left: [3, 4, 5, 6, 1, 2]


def left_rotate_by_k(nums, k):
    temp_arr = []
    n = len(nums)
    k = k % n

    temp_arr = nums[:k]
    for i in range(k, n):
        nums[i-k] = nums[i]
    
    for i in range(n - k, n):
        nums[i] = temp_arr[i - (n - k)]
    return nums

def left_rotate_using_reverse(nums, d):
    n = len(nums) - 1

    # Step 1: reverse first d elements
    nums[:d] = nums[:d][::-1]

    # Step 2: reverse from d+2 to n
    nums[d+2:n+1] = nums[d+2:n+1][::-1]

    # Step 3: reverse the whole array
    nums[:] = nums[::-1]

    return nums

# print(left_rotate_by_k([1, 2, 3, 4, 5, 6], 2))
print(left_rotate_using_reverse([1, 2, 3, 4, 5, 6], 2))

