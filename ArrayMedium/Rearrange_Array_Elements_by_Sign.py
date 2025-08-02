# There’s an array ‘A’ of size ‘N’ with an equal number of positive and negative elements. Without altering the relative order of positive and negative elements, you must return an array of alternately positive and negative values.

# Note: Start the array with positive elements.

# Examples: 

# Example 1:

# Input:
# arr[] = {1,2,-4,-5}, N = 4
# Output:
# 1 -4 2 -5

# Explanation: 

# Positive elements = 1,2
# Negative elements = -4,-5
# To maintain relative ordering, 1 must occur before 2, and -4 must occur before -5.

# Example 2:
# Input:
# arr[] = {1,2,-3,-1,-2,-3}, N = 6
# Output:
# 1 -3 2 -1 3 -2
# Explanation: 

# Positive elements = 1,2,3
# Negative elements = -3,-1,-2
# To maintain relative ordering, 1 must occur before 2, and 2 must occur before 3.
# Also, -3 should come before -1, and -1 should come before -2.


def rearrange_brute(nums):
    pos_list = []
    neg_list = []

    for i in  range(len(nums)):
        if nums[i] < 0:
            neg_list.append(nums[i])
        else:
            pos_list.append(nums[i])
    
    for i in range(int(len(nums)/2)):
        nums[2 * i] = pos_list[i]
        nums[2 * i + 1] = neg_list[i]
    
    return nums

# print(rearrange_brute([1,2,-4,-5]))

def rearrange_sub_optimal(nums):
    re_arranged_list = [None] * len(nums)
    pos_index = 0
    neg_index = 1
    
    for i in range(len(nums)):
        if nums[i] < 0:
            re_arranged_list[neg_index] = nums[i]
            neg_index += 2
        else:
            re_arranged_list[pos_index]  = nums[i]
            pos_index += 2
    
    return re_arranged_list

# print(rearrange_sub_optimal([1,2,-4,-5]))


def alternate_number(nums):
    pos_list = []
    neg_list = []

    for i in range(len(nums)):
        if nums[i] < 0:
            neg_list.append(nums[i])
        else:
            pos_list.append(nums[i])
    
    if len(pos_list) > len(neg_list):
        for i in range(len(neg_list)):
            nums[i * 2] = pos_list[i]
            nums[i * 2 + 1] = neg_list[i]
        
        index = len(neg_list) * 2
        for i in range(len(neg_list), len(pos_list)):
            nums[index] = pos_list[i]
            index += 1
    else:
        for i in range(len(pos_list)):
            nums[i * 2] = pos_list[i]
            nums[i * 2 + 1] = neg_list[i]
        
        index = len(pos_list) * 2
        for i in range(len(pos_list), len(neg_list)):
            nums[index] = neg_list[i]
            index += 1
    return nums

print(alternate_number([1,2,-4,-5]))