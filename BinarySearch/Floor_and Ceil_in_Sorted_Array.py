# Problem Statement: You're given an sorted array arr of n integers and an integer x. Find the floor and ceiling of x in arr[0..n-1].
# The floor of x is the largest element in the array which is smaller than or equal to x. 
# The ceiling of x is the smallest element in the array greater than or equal to x. 

# Floor :- largest no in arry <= x
# Ceil :- smallest no in array >= x

# Example 1:
# Input Format: n = 6, arr[] ={3, 4, 4, 7, 8, 10}, x= 5
# Result: 4 7
# Explanation: The floor of 5 in the array is 4, and the ceiling of 5 in the array is 7.

# Example 2:
# Input Format: n = 6, arr[] ={3, 4, 4, 7, 8, 10}, x= 8
# Result: 8 8
# Explanation: The floor of 8 in the array is 8, and the ceiling of 8 in the array is also 8.


arr = [3, 4, 4, 7, 8, 10]
target = 5

arr2 = [3, 4, 4, 7, 8, 10]
target2 = 8

# or lower bound
def findCeil(arr, target):
    low = 0
    high = len(arr)-1
    result = -1

    while(low <= high):
        mid = (low+high)//2

        if arr[mid] >= target:
            result = arr[mid]
            high = mid-1
        else:
            low = mid + 1
    
    return result

def findFloor(arr, target):
    low = 0
    high = len(arr)-1
    result = -1

    while(low <= high):
        mid = (low+high) //2

        if arr[mid] <= target:
            result = arr[mid]
            low = mid + 1
        else:
            high = mid - 1
    
    return result

print(findFloor(arr, target))
print(findCeil(arr, target))
print(findFloor(arr2, target2))
print(findCeil(arr2, target2))


