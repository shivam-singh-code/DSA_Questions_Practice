# Given an integer array nums, find the subarray with the largest sum and return the sum of the elements present in that subarray.



# A subarray is a contiguous non-empty sequence of elements within an array.


# Examples:
# Input: nums = [2, 3, 5, -2, 7, -4]

# Output: 15

# Explanation: The subarray from index 0 to index 4 has the largest sum = 15

# Input: nums = [-2, -3, -7, -2, -10, -4]

# Output: -2

# Explanation: The element on index 0 or index 3 make up the largest sum when taken as a subarray

def find_max_sum_subarray(nums):
    sum = -100000
    maxi = -100000
    
    start  = 0
    
    
    for i in range(len(nums)):
        if sum == 0:
            start = i
        sum = sum + nums[i]
        if sum > maxi:
            maxi = sum
            ans_start = start
            ans_end = i
            
        if sum < 0:
            sum = 0
    
    return maxi

print(find_max_sum_subarray([-2, -3, -7, -2, -10, -4]))