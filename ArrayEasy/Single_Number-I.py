# Given an array of nums of n integers. Every integer in the array appears twice except one integer. Find the number that appeared once in the array.


# Examples:
# Input : nums = [1, 2, 2, 4, 3, 1, 4]

# Output : 3

# Explanation : The integer 3 has appeared only once.

# Brute Forece Approach
# Time complexity O(n)
def single_number_brute(nums):
    for i in range(len(nums)):
        num = nums[i]
        counter = 0
        for j in range(len(nums)):
            if (nums[i] == nums[j]):
                counter += 1
        if counter == 1:
            return nums[i]
        
# print(single_number_brute([1, 2, 2, 4, 3, 1, 4]))
        

# Sub-optimal or better approach
# use hash but better in case of large input 
# Then use dicitionary to keep track of value and their occurrence


# Optimal solution with xor
def single_number_optimal(nums):
    xor = 0
    for i in range(len(nums)):
        xor = xor ^ nums[i]
    return xor

# print(single_number_optimal([1, 2, 2, 4, 3, 1, 4]))
# print(single_number_optimal([5]))
print(single_number_optimal([1, 2, 2, 7, 3, 3, 1, 4, 4]))