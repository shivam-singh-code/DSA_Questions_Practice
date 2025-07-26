# Given an integer array nums of size n, return the majority element of the array.



# The majority element of an array is an element that appears more than n/2 times in the array. The array is guaranteed to have a majority element.


# Examples:
# Input: nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]

# Output: 7

# Explanation: The number 7 appears 5 times in the 9 sized array

# Input: nums = [1, 1, 1, 2, 1, 2]

# Output: 1

# Explanation: The number 1 appears 4 times in the 6 sized array

from collections import Counter


# Better apporach time complexity of O(n) but space compelxity is O(n)
def find_majority_element(arr):
    n = len(arr)
    
    count = Counter(arr)
    
    for num, count in count.items():
        if count > (n//2):
            return num
        
# print(find_majority_element([7, 0, 0, 1, 7, 7, 2, 7, 7]))


# Optimal Apporach Moore's Voting ALogrithm
def find_majority_element_Optimal(arr):
    cnt = 0
    el = None
    
    for i in range(len(arr)):
        if cnt == 0:
            cnt = 1
            el = arr[i]
        elif arr[i] == el:
            cnt += 1
        else:
            cnt -= 1
    
    cnt2 = 0
    for i in range(len(arr)):
        if arr[i] == el:
            cnt2 += 1
    
    if cnt2 > (len(arr)//2):
        return el
    
    return -1


print(find_majority_element_Optimal([7, 0, 0, 1, 7, 7, 2, 7, 7]))
print(find_majority_element_Optimal([1, 1, 1, 2, 1, 2]))