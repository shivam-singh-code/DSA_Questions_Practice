# Problem Statement: Given an array of integers and an integer k, return the total number of subarrays whose sum equals k.

# A subarray is a contiguous non-empty sequence of elements within an array.

# Examples

# Example 1:
# Input Format: N = 4, array[] = {3, 1, 2, 4}, k = 6
# Result: 2
# Explanation: The subarrays that sum up to 6 are [3, 1, 2] and [2, 4].

# Example 2:
# Input Format: N = 3, array[] = {1,2,3}, k = 3
# Result: 2
# Explanation: The subarrays that sum up to 3 are [1, 2], and [3].

from collections import defaultdict

def find_all_subArray_with_griven_sum(arr, k):
    n = len(arr)
    mpp = defaultdict(int)
    presum = 0
    cnt = 0
    
    mpp[0] = 1
    for i in range(n):
        # add current element to presum
        presum += arr[i]
        print(f"Presum: {presum}")
        
        # Calculate x - k
        remove = presum  - k
        print(remove)
        # Add the number of subarray to be removed
        print(f"mpp[remove] {mpp[remove]}")
        cnt += mpp[remove]
        print(f"count val {cnt}\n")

        # Update the count of prefix sum
        # in the map.
        mpp[presum] += 1
    
    return cnt


arr = [3, 1, 2, 4]
k = 6
cnt = find_all_subArray_with_griven_sum(arr, k)
print("The number of subarrays is:", cnt)