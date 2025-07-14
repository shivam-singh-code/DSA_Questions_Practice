# Given an integer array of size n containing distinct values in the range from 0 to n (inclusive), return the only number missing from the array within this range.


# Examples:
# Input: nums = [0, 2, 3, 1, 4]

# Output: 5

# Explanation: nums contains 0, 1, 2, 3, 4 thus leaving 5 as the only missing number in the range [0, 5]


# Brute Force method
def find_missing_number_b(nums):
    for i in range(len(nums)+1):
        flag = 0
        for j in range(len(nums)):
            if nums[j] == i:
                flag = 1
                break
        
        if flag == 0:
            return i
        
# print(find_missing_number_b([0, 2, 3, 1, 4]))


# Better method hashing
def find_missing_number_hashing(nums):
    hash_val = [0] * (len(nums)+1)
    for i in range(len(nums)):
        hash_val[nums[i]] = 1
    
    # print(f"Hash array : {hash_val}")

    for i in range(len(nums)+1):
        if hash_val[i] == 0:
            return i
        

# print(find_missing_number_hashing([0, 2, 3, 1, 4]))


# Optimal approach 1
def find_missing_number_o1(nums):
    n = len(nums)
    sum_of_array = int(n*(n+1) / 2)
    sum2 = 0
    # print(f"sum of array: {sum_of_array}")
    for i in range(len(nums)):
        sum2 += nums[i]
    return sum_of_array - sum2

# print(find_missing_number_o1([0, 2, 3, 1, 4]))


# Optimal approach2
def find_missing_number_o2(nums):
    xor1 = 0
    for i in range(len(nums)+1):
        xor1 = xor1 ^ i
    
    xor2 = 0
    for i in range(len(nums)):
        xor2 = xor2 ^ i
    
    return xor1 ^ xor2

print(find_missing_number_o2([0, 2, 3, 1, 4]))