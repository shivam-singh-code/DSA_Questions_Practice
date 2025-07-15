# Given an array nums of size n and an integer k, find the length of the longest sub-array that sums to k. If no such sub-array exists, return 0.


# Examples:
# Input: nums = [10, 5, 2, 7, 1, 9],  k=15

# Output: 4

# Explanation: The longest sub-array with a sum equal to 15 is [5, 2, 7, 1], which has a length of 4. This sub-array starts at index 1 and ends at index 4, and the sum of its elements (5 + 2 + 7 + 1) equals 15. Therefore, the length of this sub-array is 4.


# Better approach
def longest_sub_array_with_sum_k(a, k):
    n = len(a)

    preSumMap = {}
    Sum = 0
    maxLen = 0

    for i in range(n):
        # Calculate the prefix sum till index  i:
        Sum += a[i]

        # if the sum = k, update the maxLen:
        if Sum == k:
            maxLen = max(maxLen, i+1)

        # calculate the sum of the remaining part i.e x-k
        rem = Sum - k

        # Calculate the length and update the maxLen:
        if rem in preSumMap:
            length = i - preSumMap[rem]
            maxLen = max(maxLen, length)
        
        # Finally update the map checking the conditions:
        if Sum not in preSumMap:
            preSumMap[Sum] = i
        
    return maxLen

a = [2, 3, 5, 1, 9]
k = 10

# print(longest_sub_array_with_sum_k(a, k))


# Optimal approach work only for postive and zeroes
def longest_sub_array_with_sum_k_optimal(a, k):
    n = len(a)
    maxLen = 0
    Sum = a[0]
    left = 0
    right = 0

    while (right < n):
        while(left <= right and Sum > k):
            Sum -= a[left]
            left += 1
        
        if (Sum == k):
            maxLen = max(maxLen, right - left + 1)
        
        right += 1
        if right < n:
            Sum += a[right]
    
    return maxLen

print(longest_sub_array_with_sum_k_optimal(a, k))