# Given an array nums consisting of only 0, 1, or 2. Sort the array in non-decreasing order. The sorting must be done in-place, without making a copy of the original array.


# Examples:
# Input: nums = [1, 0, 2, 1, 0]

# Output: [0, 0, 1, 1, 2]

# Explanation: The nums array in sorted order has 2 zeroes, 2 ones and 1 two

# Input: nums = [0, 0, 1, 1, 1]

# Output: [0, 0, 1, 1, 1]

# Explanation: The nums array in sorted order has 2 zeroes, 3 ones and zero twos


# better apporach time complexity o(n) space O(1)
def sort0_1_2_better(nums):
    zero_counter, one_counter, two_counter  = 0, 0 ,0
    for i in range(len(nums)):
        if nums[i] == 0:
            zero_counter += 1
        elif nums[i] == 1:
            one_counter += 1
        else:
            two_counter += 1

    for i in range(zero_counter):
        nums[i] = 0
    
    for i in range(zero_counter, (zero_counter + one_counter)):
        nums[i] = 1

    for i in range((zero_counter + one_counter), len(nums)):
        nums[i] = 2

    return nums


# print(sort0_1_2_better([1, 0, 2, 1, 0])) #[0, 0, 1, 1, 2]
# print(sort0_1_2_better([0, 0, 1, 1, 1])) #[0, 0, 1, 1, 1]


# Optimal approach using Dutch National Flag Alogrithm
def sort0_1_2_optimal(nums):
    low = 0
    mid = 0
    high = len(nums) - 1

    while(mid <= high):
        if nums[mid] == 0:
            swap(nums, low, mid)
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            swap(nums, mid, high)
            high -= 1

    return nums

def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp


print(sort0_1_2_optimal([1, 0, 2, 1, 0])) #[0, 0, 1, 1, 2]
print(sort0_1_2_optimal([0, 0, 1, 1, 1])) #[0, 0, 1, 1, 1]
