# Problem Statement: Given an array Arr[] of integers, rearrange the numbers of the given array into the lexicographically next greater permutation of numbers.

# If such an arrangement is not possible, it must rearrange to the lowest possible order (i.e., sorted in ascending order).

# Examples
# Example 1 :

# Input format: Arr[] = {1,3,2}
# Output: Arr[] = {2,1,3}
# Explanation: All permutations of {1,2,3} are {{1,2,3} , {1,3,2}, {2,13} , {2,3,1} , {3,1,2} , {3,2,1}}. So, the next permutation just after {1,3,2} is {2,1,3}.
# Example 2:

# Input format: Arr[] = {3,2,1}
# Output: Arr[] = {1,2,3}
# Explanation: As we see all permutations of {1,2,3}, we find {3,2,1} at the last position. So, we have to return the topmost permutation.

def next_permutation(a):
    ind = -1
    n = len(a)

    for i in range(n-2, -1, -1):
        if a[i] < a[i+1]:
            ind = i
            break
    
    if (ind == -1):
        a.reverse()
        return a
       
    for i in range(n-1, ind, -1):
        if a[i] > a[ind]:
            a[i], a[ind] = a[ind], a[i]
            break
    
    a[ind+1:] = reversed(a[ind+1:])
    return a

print(next_permutation([2, 1, 5, 4, 3, 0, 0]))
