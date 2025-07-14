# Given a binary array nums, return the maximum number of consecutive 1s in the array.



# A binary array is an array that contains only 0s and 1s.


# Examples:
# Input: nums = [1, 1, 0, 0, 1, 1, 1, 0]

# Output: 3

# Explanation: The maximum consecutive 1s are present from index 4 to index 6, amounting to 3 1s


def find_max_conse_ones(nums):
    max_no_of_ones = 0
    counter = 0

    for i in range(len(nums)):
        if nums[i] == 1:
            counter += 1
        else:
            counter = 0
        
        if counter > max_no_of_ones:
            max_no_of_ones = counter
    
    return max_no_of_ones


print(find_max_conse_ones([1, 1, 0, 0, 1, 1, 1, 0]))
print(find_max_conse_ones([0, 0, 0, 0, 0, 0, 0, 0]))