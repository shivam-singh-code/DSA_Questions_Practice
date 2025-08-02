# Problem Statement: Given an array, print all the elements which are leaders. A Leader is an element that is greater than all of the elements on its right side in the array.
# Examples

# Example 1:
# Input:
#  arr = [4, 7, 1, 0]
# Output:
#  7 1 0
# Explanation:
#  Rightmost element is always a leader. 7 and 1 are greater than the elements in their right side.

# Example 2:
# Input:
#  arr = [10, 22, 12, 3, 0, 6]
# Output:
#  22 12 6
# Explanation:
#  6 is a leader. In addition to that, 12 is greater than all the elements in its right side (3, 0, 6), also 22 is greater than 12, 3, 0, 6.

import sys 

def find_leaders(a):
    maximum = -sys.maxsize - 1
    leader_list = []
    for i in range(len(a)-1, -1, -1):
        if a[i] > maximum:
            leader_list.append(a[i])
        
        maximum = max(maximum, a[i])
    return leader_list

print(find_leaders([10, 22, 12, 3, 0, 6]))
