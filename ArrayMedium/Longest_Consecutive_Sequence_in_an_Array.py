# Problem Statement: You are given an array of ‘N’ integers. You need to find the length of the longest sequence which contains the consecutive elements.

# Examples

# Example 1:

# Input: [100, 200, 1, 3, 2, 4]

# Output: 4

# Explanation: The longest consecutive subsequence is 1, 2, 3, and 4.

# Input: [3, 8, 5, 7, 6]

# Output: 4

# Explanation: The longest consecutive subsequence is 5, 6, 7, and 8.

import sys

def find_longest_conse_better(a):
    if len(a) == 0:
        return 0
    
    a.sort()

    last_smallest = -sys.maxsize - 1
    cnt = 0
    longest = 1
    
    for i in range(len(a)):
        if a[i] - 1 == last_smallest:
            cnt += 1
            last_smallest = a[i]
        elif last_smallest != a[i]:
            cnt = 1
            last_smallest = a[i]
        
        longest = max(longest, cnt)
    
    return longest

# print(find_longest_conse_better([100, 200, 1, 3, 2, 4]))
# print(find_longest_conse_better([3, 8, 5, 7, 6]))


def find_longest_conse_optimal(nums):
    n = len(nums)
    if n == 0: return 0

    longest = 1
    st = set()

    for i in range(n):
        st.add(nums[i])

    for it in st:
        if it - 1 not in st:
            cnt = 1
            x = it

            while x + 1 in st:
                cnt += 1
                x += 1
            
            longest = max(longest, cnt)

    return longest        

print(find_longest_conse_optimal([100, 200, 1, 2, 3, 4]))